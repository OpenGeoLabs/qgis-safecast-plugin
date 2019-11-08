"""
/***************************************************************************
                             A QGIS Safecast Plugin
                             ----------------------
        begin                : 2016-05-25
        git sha              : $Format:%H$
        copyright            : (C) 2016-2018 by OpenGeoLabs s.r.o.
        acknowledgement      : Suro, Czech Republic
        email                : martin.landa@opengeolabs.cz
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import os
import sys
import time
from datetime import datetime, timedelta, date
from dateutil import tz

from PyQt5.QtWidgets import QProgressBar

from qgis.core import QgsVectorLayer, QgsField, QgsFeature, \
    QgsGeometry, QgsPointXY, QgsFields, \
    QgsCoordinateReferenceSystem, QgsMessageLog, QgsDistanceArea
from qgis.utils import iface, Qgis

from osgeo import ogr

from . import LayerBase, LayerType

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from plugin_type import PLUGIN_NAME
from style.safecast import SafecastStyle

class SafecastWriterError(Exception):
    """Safecast writer error class.
    """
    pass

class SafecastLayer(LayerBase):
    def __init__(self, fileName, storageFormat):
        """Safecast memory-based read-only layer.

        :param fileName: path to input file
        :param storageFormat: storage format for layer (Memory or SQLite)
        """
        super(SafecastLayer, self).__init__(fileName, storageFormat)

        # define attributes
        self._aliases = self._setAttrbsDefs()
        # skip computed attributes
        # - FID (SQLite only)
        # - ader_microsvh
        # - time_local
        # - speed_kmph
        # - dose_increment
        # - time_cumulative
        # - dose_cumulative
        self.skipNumAttrbs = 6
        # two last columns split (hdop + checksum)
        self._validNumAttrbs = len(self.attributeList()) - (self.skipNumAttrbs + 1)

        # metadata
        self.setAttribution('Safecast plugin')
        self.setAttributionUrl('https://opengeolabs.github.io/qgis-safecast-plugin')

        # layer type
        self.layerType = LayerType.Safecast

        # style
        self._style = SafecastStyle()

    def load(self, reader):
        """Load LOG file using specified reader.

        LoadError is raised on failure.

        :param reader: reader class used for reading input data
        """
        # store metadata
        self.metadata = {
            'table': 'safecast_metadata',
            'columns': {
                'format': reader.format_version,
                'deadtime': reader.deadtime
            }
        }

        super(SafecastLayer, self).load(reader)

    def _item2feat(self, item):
        """Process line in LOG file and create a new point feature based on this line.

        :param item: item to be processed
        """
        # define internal functions first
        def coords_float(coord, ne):
            """Convert coordinates to DMS.

            :param coord: coordinates as a string
            :param ne: longitude/latitude indicator

            :return: coordinate value
            """
            ddmm, s = coord.split('.', 1)
            val = int(ddmm[:-2]) + int(ddmm[-2:])/60. + float('0.'+s)/60.
            if ne in ('S', 'W'):
                val *= -1
            return val

        if len(item) != self._validNumAttrbs:
            raise LoadError(
                self.tr("Failed to read input data. Line: {}").format(','.join(item))
            )

        # force to split last item (hdop & checksum)
        item[-1], newitem = item[-1].split('*', 1)
        item.append('*' + newitem)

        # set coordinates
        y = coords_float(item[7], item[8])
        x = coords_float(item[9], item[10])
        point = QgsPointXY(x, y)

        # check validity
        # drop data according
        # - HDOP (item[-2])
        if int(item[-2]) == 9999:
            self._addError('HDOP = 9999')
            return None
        # - SAT (item[-3])
        if int(item[-3]) < 3:
            self._addError('SAT < 3')
            return None
        ### Date validity will be performed when whole file loaded
        # - year (item[2])
        # myear = datetime2year(item[2])
        # minyear = 2011
        # maxyear = datetime.now().year
        # if myear < minyear or myear > maxyear:
        #     self._addError('year <> {0}-{1}'.format(
        #         minyear, maxyear
        #     ))
        #     return None

        # check timestamp (hours only, dates are fixed when
        # recalculating attributes) validity
        try:
            datetime.strptime(item[2].split('T', 1)[1], "%H:%M:%SZ")
        except ValueError as e:
            self._addError('invalid timestamp {}'.format(item[2]))
            return None

        # - null island
        if abs(x) < sys.float_info.epsilon or \
           abs(y) < sys.float_info.epsilon:
            self._addError('null island')
            return None

        # compute ader_microSvh
        try:
            pulse5s = int(item[4])
            if pulse5s > 0:
                ader = pulse5s * 12
            else:
                ader = int(item[3]) # cpm
            ader *= 0.0029940119760479
        except ValueError:
            ader = -1
        # workaround: setting up precision causes in QGIS 2
        # problems when exporing data into other formats, see
        # https://lists.osgeo.org/pipermail/qgis-developer/2017-December/050969.html
        # disabled
        # see https://bitbucket.org/opengeolabs/qgis-safecast-plugin-dev/issues/14/decrease-the-number-of-decimal-places-in
        # item.insert(0, float('{0:.4f}'.format(ader)))
        item.insert(0, ader)

        # local time will be calculated after loading whole file
        item.insert(1, None)

        # speed will be calculated after loading whole file
        item.insert(2, None)

        # dose increment + time/dose cumulative will be calculated after loading whole file
        item.insert(3, None)
        item.insert(4, None)
        item.insert(5, None)

        # create new feature
        feat = QgsFeature()
        feat.setGeometry(QgsGeometry.fromPointXY(point))

        # set attributes
        feat.setAttributes(item)

        return feat

class SafecastLayerHelper(object):
    def __init__(self, layer):
        self._layer = layer
        if isinstance(layer, SafecastLayer):
            self._storageFormat = layer.storageFormat
            self._skipNumAttrbs = 6 if self._storageFormat == 'memory' else 7
            self._fileName = layer._fileName
        else:
            # assuming SQLite
            self._storageFormat = "SQLite"
            # better to be stored in metadata than hardcoded
            self._skipNumAttrbs = 7
            self._fileName = layer.dataProvider().dataSourceUri().split('|')[0]

        # ader statistics
        self._updateStats()

        # ader plot
        self._plot = [[], []]

        # create object for distance computation
        self._distance = QgsDistanceArea()
        ### self._distance.setEllipsoidalMode(True)
        self._distance.setEllipsoid('WGS84')

        # connects
        # self._layer.beforeCommitChanges.connect(self.recalculateAttributes)

    def path(self):
        """Return layer file directory path.

        :return: path as a string
        """
        return os.path.dirname(self._fileName)

    def filename(self):
        """Return layer file name without extension.

        :return: filename as a string
        """
        return os.path.splitext(
            os.path.basename(self._fileName)
        )[0]

    def _gpsChecksum(self, item):
        """Compute checksum of item.

        :param item: item line

        :return: checksum
        """
        chk = ord(item[0])

        for ichk in item[1:]:
            chk ^= ord(ichk)

        return hex(chk)[2:].upper()

    def _getMetadata(self):
        """Get metadata."""
        if isinstance(self._layer, SafecastLayer):
            return self._layer.metadata

        metadata = {}
        try:
            ds = ogr.Open(self._fileName)
            layer = ds.GetLayerByName('safecast_metadata')
            if layer:
                layer_defn = layer.GetLayerDefn()
                layer.ResetReading()
                feat = layer.GetNextFeature()
                for i in range(layer_defn.GetFieldCount()):
                    name = layer_defn.GetFieldDefn(i).GetName()
                    value = feat.GetField(i)
                    metadata[name] = value
            ds = None
        except:
            raise LoadError(
                self.tr("Unable to retrive Safecast metadata for selected layer")
            )

        return metadata
        
    def save(self, filePath):
        """Save layer to a new LOG file.

        Raises SafecastWriterError on failure.

        :param filePath: name for output file
        """
        try:
            with open(filePath, 'w') as f:
                f.write('# NEW LOG\n')
                metadata = self._getMetadata()
                f.write('# format={}\n'.format(metadata['columns']['format']))
                f.write('# deadtime={}\n'.format(metadata['columns']['deadtime']))
                features = self._layer.getFeatures()
                for feat in features:
                    attrs = feat.attributes()
                    item = ''
                    for val in attrs[self._skipNumAttrbs:-2]: # skip calculated points
                        item += '{},'.format(val)
                    item += '{}'.format(attrs[-2])
                    # join two last columns(hdop+checksum)
                    checksum = self._gpsChecksum(item[1:]) # skip '$'
                    item += '*{}\n'.format(checksum)
                    f.write(item)
        except IOError as e:
            raise SafecastWriterError(e)

    def _updateStats(self, data=None):
        """Update ader statistics.

        :param ader: ader statistics
        """
        if data:
            self._stats = data
        else:
            self._stats = {
                'count' : 0,
                'radiation': {
                    'max' : None,
                    'avg' : None,
                    'total': None,
                },
                'route': {
                    'speed' : None,
                    'time': None,
                    'distance' : None,
                }
            }

    def stats(self):
        """Get layer statistics"""
        return self._stats

    def plotData(self):
        return self._plot

    def _validateDate(self, feat_datetime, prev_datetime, first_valid_date):
        """Validate date.

        :param feat_datetime: date to be validated
        :param prev_datetime: previous date or None
        :param first_valid_date: first valid date (if prev_datetime is None)

        :return: validate date, update flag
        """
        if self._checkDate(feat_datetime):
            return feat_datetime, False

        if prev_datetime:
            timediff = self._datetimediff(
                prev_datetime, feat_datetime, timeonly=True
            ).total_seconds()
            fdate = datetime.strptime(
                prev_datetime, "%Y-%m-%dT%H:%M:%SZ"
            ).date()
        else:
            timediff = 0
            fdate = first_valid_date

        if timediff < 0:
            # next date
            fdate += timedelta(days=1)

        return datetime.strftime(
            datetime.combine(
                fdate,
                datetime.strptime(feat_datetime.split('T', 1)[1], "%H:%M:%SZ").time()
            ),
            '%Y-%m-%dT%H:%M:%SZ'
        ), True

    def _datetime2localtime(self, datetime_value):
        """Convert datetime value to local time.

        :datetime_value: date time value (eg. '2016-05-16T18:22:26Z')

        :return: local time as a string (eg. '20:22:26')
        """
        from_zone = tz.tzutc()
        to_zone = tz.tzlocal()

        utc = datetime.strptime(datetime_value, '%Y-%m-%dT%H:%M:%SZ')
        utc = utc.replace(tzinfo=from_zone)
        local = utc.astimezone(to_zone)

        return local.strftime('%H:%M:%S')

    def _checkDate(self, fdate):
        """Check if date is valid.

        :param fdate: date to be checked

        :return: True if date is valid otherwise False
        """
        minyear = 2011
        maxyear = datetime.now().year
        myear = self._datetime2year(fdate)
        if myear < minyear or myear > maxyear:
            return False
        return True

    def _datetime2year(self, datetime_value):
        """Convert datatime value to year.

        :datetime_value: date time value (eg. '2016-05-16T18:22:26Z')

        :return: local time as a int (2016)
        """
        try:
            return datetime.strptime(
                datetime_value, '%Y-%m-%dT%H:%M:%SZ'
            ).year
        except ValueError:
            return 0

    def _datetimediff(self, datetime_value1, datetime_value2, timeonly=False):
        """Compute datetime difference in sec.

        :param datetime_value1: first value
        :param datetime_value2: second value

        :return: time difference in sec
        """
        if timeonly:
            t1 = datetime.strptime(datetime_value1.split('T', 1)[1], '%H:%M:%SZ')
            t2 = datetime.strptime(datetime_value2.split('T', 1)[1], '%H:%M:%SZ')
            val1 = datetime.combine(date.today(), t1.time())
            val2 = datetime.combine(date.today(), t2.time())
        else:
            val1 = datetime.strptime(datetime_value1, '%Y-%m-%dT%H:%M:%SZ')
            val2 = datetime.strptime(datetime_value2, '%Y-%m-%dT%H:%M:%SZ')

        return val2 - val1

    def recalculateAttributes(self, only_stats=False):
        """Update attributes after loading or editing.

        :param only_stats: True for dry run (do not update attributes, only stats computed)
        """
        def td2str(td):
            """Convert timedelta objects to a HH:MM string with (+/-) sign

            Taken from: https://stackoverflow.com/questions/538666/python-format-timedelta-to-string
            """
            tdhours, rem = divmod(td.total_seconds(), 3600)
            tdminutes, rem = divmod(rem, 60)

            return '{0:02d}:{1:02d}:{2:02d}'.format(
                int(tdhours), int(tdminutes), int(rem)
            )

        idx = 0
        field_idx = {}
        for name in [ "dose_increment",
                      "time_cumulative",
                      "dose_cumulative",
                      "speed_kmph",
                      "time_local",
                      "date_time"]:
            field_idx[name] = self._layer.dataProvider().fieldNameIndex(name)

        prev = None     # previous feature

        dose_inc = None
        time_cum = 0
        dose_cum = None
        timediff = None
        speed = None
        count = 0

        # fix first valid datetime
        first_valid_date = None
        features = self._layer.getFeatures()
        for feat in features:
            fdate_time = feat.attribute("date_time")
            if self._checkDate(fdate_time):
                first_valid_date = datetime.strptime(fdate_time, "%Y-%m-%dT%H:%M:%SZ").date()
                break

        if first_valid_date is None:
            iface.messageBar().pushMessage(
                self._layer.tr("Warning"),
                self._layer.tr("No valid date found. Unable to fix datetime."),
                level=Qgis.Warning,
                duration=5
            )

        if not only_stats:
            self._layer.setReadOnly(False)
            self._layer.startEditing()

        prev_datetime = None
        features = self._layer.getFeatures()
        updated_attrs = {}

        ader_max = None
        ader_cum = 0
        speed_cum = 0
        dist_cum = 0
        self._plot = [[], []]
        start = time.clock()
        for feat in features:
            feat_datetime = feat.attribute("date_time")
            # fix date if invalid
            feat_datetime, newdt = self._validateDate(feat_datetime, prev_datetime, first_valid_date)

            # compute ader stats
            ader = feat.attribute("ader_microsvh")
            if ader_max is None or ader_max < ader:
                ader_max = ader
            ader_cum += ader

            # compute local time (from datetime)
            try:
                time_local = self._datetime2localtime(feat_datetime)
            except ValueError:
                time_local = self._layer.tr("unknown")

            if prev:
                timediff = self._datetimediff(
                    prev_datetime,
                    feat_datetime
                ).total_seconds() / (60 * 60)

                dose_inc = ader * timediff

                # speed
                dist = self._distance.measureLine(
                    feat.geometry().asPoint(),
                    prev.geometry().asPoint()
                )
                dist_cum += dist

                # workaround: setting up precision causes in QGIS 2
                # problems when exporing data into other formats, see
                # https://lists.osgeo.org/pipermail/qgis-developer/2017-December/050969.html
                # disabled
                # see https://bitbucket.org/opengeolabs/qgis-safecast-plugin-dev/issues/14/decrease-the-number-of-decimal-places-in
                # speed = float('{0:.2f}'.format((dist / 1e3) / timediff)) # kmph
                if timediff > 0:
                    speed = (dist / 1e3) / timediff # kmph
                else:
                    speed = 0
                speed_cum += speed

                # time cumulative
                time_cum += timediff

            if dose_inc:
                if dose_cum is None:
                    dose_cum = 0
                dose_cum += dose_inc


            # set previous feature for next run
            prev = feat
            prev_datetime = feat_datetime

            # update plot data
            self._plot[0].append(dist_cum / 1000) # km
            self._plot[1].append(ader)

            # update attributes
            attrs = { "dose_increment" : dose_inc,
                      "time_cumulative": td2str(timedelta(hours=time_cum)),
                      "dose_cumulative": dose_cum,
                      "speed_kmph": speed,
                      "time_local": time_local,
            }
            if newdt:
                attrs["date_time"] = feat_datetime

            count += 1
            if only_stats:
                continue

            updated = {}
            for name, value in list(attrs.items()):
                updated[field_idx[name]] = value
            updated_attrs[feat.id()] = updated

        self._layer.dataProvider().changeAttributeValues(updated_attrs)

        # update layer internal statistics
        if count > 0:
            self._updateStats({
                'count' : count,
                'radiation': {
                    'max' : ader_max,
                    'avg' : ader_cum / count,
                    'total': dose_cum,
                },
                'route': {
                    'speed' : speed_cum / count,
                    'time': td2str(timedelta(hours=time_cum)),
                    'distance' : dist_cum,
                }
            })
        else:
            self._updateStats()

        # save changes
        if not only_stats:
            self._layer.commitChanges()
            self._layer.setReadOnly(True)

            # force reload attributes
            self._layer.dataProvider().forceReload()

            # QgsMessageLog.logMessage(
            #     '{0}: {1} features updated in {2:.2f} sec'.format(
            #         self._layer.name(), self._layer.featureCount(), time.clock() - start),
            #     tag=PLUGIN_NAME,
            #     level=Qgis.Info
            # )

    def computeStats(self):
        self.recalculateAttributes(only_stats=False)
