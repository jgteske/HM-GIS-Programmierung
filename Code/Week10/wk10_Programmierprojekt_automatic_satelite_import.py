# -*- coding: utf-8 -*-

"""
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (
    QgsProcessing,
    QgsFeatureSink,
    QgsProcessingException,
    QgsProcessingAlgorithm,
    QgsProcessingParameterFeatureSource,
    QgsProcessingParameterVectorLayer,
    QgsProcessingParameterFeatureSink,
)
from qgis import processing


class ExampleAlgo(QgsProcessingAlgorithm):
    """
    This is an example algorithm that takes a vector layer and
    creates a new identical one.

    It is meant to be used as an example of how to create your own
    algorithms and explain methods and variables used to do it. An
    algorithm like this will be available in all elements, and there
    is not need for additional work.

    All Processing algorithms should extend the QgsProcessingAlgorithm
    class.
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    # INPUT = "INPUT"
    OUTPUT = "OUTPUT"

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate("Processing", string)

    def createInstance(self):
        return ExampleAlgo()

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return "satimport"

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr("Satelite Import")

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr("Programmierprojekt")

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return "programmierprojekt"

    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        return self.tr("Example algorithm short description")

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        """
        self.addParameter(
            QgsProcessingParameterVectorLayer(
                "input", "INPUT", types=[QgsProcessing.TypeVectorAnyGeometry]
            )
        )
        """
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                "output", "OUTPUT", type=QgsProcessing.TypeRaster
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """

        # Importing used Libraries
        import sys
        from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication, QProcess
        from qgis.PyQt.QtGui import QIcon
        from qgis.PyQt.QtWidgets import QAction, QPushButton
        from PyQt5 import QtWidgets
        from datetime import date, timedelta
        import webbrowser
        import os.path
        import os
        import json
        import requests
        import glob
        import shutil
        import zipfile
        import rasterio
        from rasterio import warp
        from rasterio import plot
        from osgeo import gdal, ogr
        import subprocess
        from pyroSAR.snap import geocode
        from sentinelsat import (
            SentinelAPI,
            geojson_to_wkt,
            read_geojson,
        )

        os.system("pause")

        """
        if self.first_start == True:
            self.first_start = False
            self.dlg = OpenSourceMultiSourceProcessorDialog()
        self.dlg.stackedWidget.setCurrentWidget(self.dlg.Schritt_Willkommen)
        self.dlg.Schritt2.setEnabled(False)
        """

        # Öffnen der erste Seite
        def Seite1(self):
            self.dlg.stackedWidget.setCurrentWidget(self.dlg.Schritt_1)
            self.dlg.Schritt1.setEnabled(False)

        """
        # Erstellen des Arbeitsverzeichnises
        def select_Workfolder(self):
            self.dlg.Button_Pfad.setEnabled(False)
            dir = QtWidgets.QFileDialog.getExistingDirectory(None, "Select a folder:")
            self.dlg.Pfad.setText(dir)
            self.Workpath = dir
            if not os.path.exists(self.Workpath):
                os.mkdir(self.Workpath)
            if not os.path.exists("" + self.Workpath + r"/Geojson"):
                os.mkdir("" + self.Workpath + r"/Geojson")
            if not os.path.exists("" + self.Workpath + r"/Downloadfiles"):
                os.mkdir("" + self.Workpath + r"/Downloadfiles")
            if not os.path.exists("" + self.Workpath + r"/EditTiles"):
                os.mkdir("" + self.Workpath + r"/EditTiles")
            if not os.path.exists("" + self.Workpath + r"/GeoTIFFs"):
                os.mkdir("" + self.Workpath + r"/GeoTIFFs")

        # Öffnen der Webseite zum Erstellen des geoJSON-Files
        def GeoJSON(self):
            webbrowser.open(r"https://geojson.io")
            self.dlg.Open_GeoJSON_Seite.setEnabled(False)
            self.dlg.Best_Button_JSON.setEnabled(True)

        # Verschieben des GeoJSON in das Arbeitsverzeichnis und Benenne es um
        def MoveGeoJSON(self):
            self.dlg.Best_Button_JSON.setEnabled(False)
            for dirpath, dirnames, filenames in os.walk(r"c:\\"):
                for filename in filenames:
                    if filename.endswith("map.geojson"):
                        shutil.move(
                            ("" + dirpath + "/" + filename + ""),
                            ("" + self.Workpath + "/Geojson/Area_of_Interest.geojson"),
                        )

            if os.path.isfile("" + self.Workpath + "/Geojson/Area_of_Interest.geojson"):
                self.dlg.Schritt2_check.setHidden(False)
                self.dlg.Schritt3.setEnabled(True)
                self.dlg.Schritt2.setEnabled(False)
                self.dlg.Schritt2.setStyleSheet("background-color: green")
                self.dlg.Schritt3.setStyleSheet("")
        """

        """
        outputs["Buffer"] = processing.run(
            "native:buffer",
            alg_params,
            context=context,
            feedback=feedback,
            is_child_algorithm=True,
        )

        return {"OUTPUT": outputs["Buffer"]["OUTPUT"]}
        """
