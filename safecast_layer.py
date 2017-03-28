"""
/***************************************************************************
                             A QGIS Safecast Plugin
                             ----------------------
        begin                : 2016-05-25
        git sha              : $Format:%H$
        copyright            : (C) 2016 by OpenGeoLabs s.r.o.
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
import time
from datetime import datetime
from dateutil import tz

from PyQt4.QtCore import QVariant
from PyQt4.QtGui import QProgressBar

from qgis.core import QgsVectorLayer, QgsField, QgsFeature, QgsGeometry, QgsPoint
from qgis.utils import iface
from qgis.gui import QgsMessageBar

from .reader import SafecastReaderError

class SafecastWriterError(Exception):
    """Safecast writer error class.
    """
    pass

class SafecastLayer(QgsVectorLayer):
    def __init__(self, fileName):
        """Safecast memory-based read-only layer.

        :param fileName: path to input file
        """
        self._fileName = fileName

        # create point layer (WGS-84, EPSG:4326)
        super(SafecastLayer, self).__init__('Point?crs=epsg:4326',
                                            os.path.splitext(os.path.basename(self._fileName))[0],
                                            'memory')

        # define list of attributes
        self._provider = self.dataProvider()
        attrbs = [QgsField("ader_microsvh", QVariant.Double),
                  QgsField("time_local", QVariant.String),
                  QgsField("device", QVariant.String),
                  QgsField("device_id",  QVariant.Int),
                  QgsField("date_time", QVariant.String),
                  QgsField("cpm", QVariant.Int),
                  QgsField("pulses5s", QVariant.Int),
                  QgsField("pulses_total", QVariant.Int),
                  QgsField("validity", QVariant.String),
                  QgsField("lat_deg", QVariant.String),
                  QgsField("hemisphere", QVariant.String),
                  QgsField("long_deg", QVariant.String),
                  QgsField("east_west", QVariant.String),
                  QgsField("altitude", QVariant.Double),
                  QgsField("gps_validity", QVariant.String),
                  QgsField("sat", QVariant.Int),
                  QgsField("hdop", QVariant.Int),
                  QgsField("checksum", QVariant.String)
        ]

        # set aliases when running QGIS 2.18+
        if hasattr(attrbs[0], "setAlias"):
            self._setAliases(attrbs)

        # set attributes
        self._provider.addAttributes(attrbs)

        self.updateFields()

        # open layer in read-only mode
        self.setReadOnly(True)

        # layer is empty, no data loaded
        self._loaded = False

    def _setAliases(self, attrbs):
        """Set aliases

        :params attrbs: list of QgsField instances
        """
        alias = [self.tr("ADER microSv/h"),
                 self.tr("Local time"),
                 self.tr("Device"),
                 self.tr("Device ID"),
                 self.tr("Datetime"),
                 self.tr("CPM"),
                 self.tr("Pulses 5sec"),
                 self.tr("Pulses total"),
                 self.tr("Validity"),
                 self.tr("Latitude (deg)"),
                 self.tr("Hemisphere"),
                 self.tr("Longitude (deg)"),
                 self.tr("East/West"),
                 self.tr("Altitude"),
                 self.tr("GPS Validity"),
                 self.tr("Sat"),
                 self.tr("HDOP"),
                 self.tr("CheckSum")
        ]
        i = 0
        for field in attrbs:
            field.setAlias(alias[i])
            i += 1

    def load(self, reader):
        """Load LOG file using specified reader.

        SafecastReaderError is raised on failure.

        :param reader: reader class used for reading input data
        """
        if self._loaded:
            return # data already loaded

        # store metadata
        self._metadata = {
            'format': reader.format_version,
            'deadtime': reader.deadtime
        }

        # create progress bar widget
        progressMessageBar = iface.messageBar().createMessage(self.tr("Loading data..."))
        progress = QProgressBar()
        progress.setMaximum(100)
        progressMessageBar.layout().addWidget(progress)
        iface.messageBar().pushWidget(progressMessageBar, iface.messageBar().INFO)

        # load items as new point features (inform user about progress)
        i = 0
        count = reader.count()
        start = time.clock()
        for f in reader:
            self._process_row(f) # add features to the map layer
            i += 1
            if i % 100 == 0:
                percent = i / float(count) * 100
                progress.setValue(percent)
        endtime = time.clock() - start
        progress.setValue(100)
        iface.messageBar().clearWidgets()

        # inform user about successfull import
        iface.messageBar().pushMessage(self.tr("Info"),
                                       self.tr("{} features loaded (in {:.2f} sec).").format(count, endtime),
                                       level=QgsMessageBar.INFO, duration=3)
        # data loaded (avoid multiple imports)
        self._loaded = True
        
    def _process_row(self, row):
        """Process line in LOG file and create a new point feature based on this line.

        :param row: row to be processed
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

        def datetime2localtime(datetime_value):
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

        if len(row) != len(self._provider.fields()) - 3:
            # last four columns (ader_microSvh, time_local, hdop, checksum) are computed
            raise SafecastReaderError(self.tr("Failed to read input data. Line: {}").format(','.join(row)))

        # force to split last item (hdop & checksum)
        row[-1], newitem = row[-1].split('*', 1)
        row.append('*' + newitem)

        # compute ader_microSvh
        try:
            ader = int(row[3]) * 0.0028571429
        except ValueError:
            ader = -1
        row.insert(0, ader)

        # compute local time (from datetime)
        try:
            time_local = datetime2localtime(row[3])
        except ValueError:
            time_local = self.tr("unknown")
        row.insert(1, time_local)

        # create new feature
        fet = QgsFeature()
        # set coordinates
        y = coords_float(row[9], row[10])
        x = coords_float(row[11], row[12])
        fet.setGeometry(QgsGeometry.fromPoint(QgsPoint(x, y)))
        # set attributes
        fet.setAttributes(row)
        # add new feature into layer
        self._provider.addFeatures([fet])

    def save(self, filePath):
        """Save layer to a new LOG file.

        Raises SafecastWriterError on failure.

        :param filePath: name for output file
        """
        try:
            with open(filePath, 'w') as f:
                f.write('# NEW LOG\n')
                f.write('# format={}\n'.format(self._metadata['format']))
                f.write('# deadtime={}\n'.format(self._metadata['deadtime']))
                features = self.getFeatures()
                for feat in features:
                    attrs = feat.attributes()
                    for val in attrs[2:-2]: # skip ader_microSvh and local time
                        f.write('{},'.format(val))
                    f.write('{}{}\n'.format(attrs[-2], attrs[-1]))
        except IOError as e:
            raise SafecastWriterError(e)

    def path(self):
        """Return layer file directory path.

        :return: path as a string
        """
        return os.path.dirname(self._fileName)
