# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DissolveWithStats
                                 A QGIS plugin
 Group entities with same value for one field, calculate statistics on the other fields
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-02-19
        copyright            : (C) 2019 by Julie Pierson, UMR 5319 Passages, CNRS
        email                : julie.pierson@cnrs.fr
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
    """Load DissolveWithStats class from file DissolveWithStats.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .dissolve_stats import DissolveWithStats
    return DissolveWithStats(iface)
