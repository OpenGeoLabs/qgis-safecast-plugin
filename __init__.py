# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Safecast
                                 A QGIS plugin
 Safecast Plugin
                             -------------------
        begin                : 2016-05-25
        copyright            : (C) 2016 by OpenGeoLabs s.r.o.
        email                : martin.landa@opengeolabs.cz
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Safecast class from file Safecast.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .radiation_toolbox import RadiationToolbox
    return RadiationToolbox(iface)
