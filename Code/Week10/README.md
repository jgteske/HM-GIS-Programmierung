# Elemente and Tipps for this Project

## Required Tools

- SNAP – ESA Science Toolbox Exploitation Platform: All Toolboxes (https://step.esa.int/main/download/snap-download/)
- Python Plugins to installed via the OSGeo4W-Shell (included in QGIS)
  - pip install
    ```
    pip install pyroSAR
    pip install sentinelsat
    pip install glob
    ```
- RasterIO: (https://www.lfd.uci.edu/~gohlke/pythonlibs/#rasterio)
  ```
  pip install >Pfad zur heruntergeladenen Datei *.whl
  pip install rasterio
  ```
---
## Imports
```python
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
```

---
## Grundlagen

Alle Elemente werden im Qt-Designer angelegt in der run()-Methode, z.B.
```PYTHON
if self.first_start == True:
self.first_start = False
self.dlg = OpenSourceMultiSourceProcessorDialog()
self.dlg.stackedWidget.setCurrentWidget(self.dlg.Schritt_Willkommen)
self.dlg.Schritt2.setEnabled(False)
```
…

• Soll ein Element sichtbar aber nicht auswählbar sein, so setzt man: <Name>.setEnabled(False)
• Soll ein Element unsichtbar sein, so setzt man: <Name>.setHidden(True)
Die Änderungen von Seite zu Seite werden über den Aufruf von Funktionen realisiert, die über die Buttons aufgerufen werden, z.B.

```PYTHON
#Öffnen der erste Seite
def Seite1(self):
self.dlg.stackedWidget.setCurrentWidget(self.dlg.Schritt_1)
self.dlg.Schritt1.setEnabled(False)
#Erstellen des Arbeitsverzeichnises
def select_Workfolder(self):
self.dlg.Button_Pfad.setEnabled(False)
dir = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select a folder:')
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
#Öffnen der Webseite zum Erstellen des geoJSON-Files
def GeoJSON(self):
webbrowser.open(r'https://geojson.io')
self.dlg.Open_GeoJSON_Seite.setEnabled(False)
self.dlg.Best_Button_JSON.setEnabled(True)
#Verschieben des GeoJSON in das Arbeitsverzeichnis und Benenne es um
def MoveGeoJSON(self):
self.dlg.Best_Button_JSON.setEnabled(False)
for dirpath, dirnames, filenames in os.walk(r"c:\\"):
for filename in filenames:
if filename.endswith("map.geojson"):
shutil.move(("" + dirpath + "/" + filename + ""), ("" + self.Workpath + "/Geojson/Area_of_Interest.geojson"))
if os.path.isfile("" + self.Workpath + "/Geojson/Area_of_Interest.geojson"):
self.dlg.Schritt2_check.setHidden(False)
self.dlg.Schritt3.setEnabled(True)
self.dlg.Schritt2.setEnabled(False)
self.dlg.Schritt2.setStyleSheet("background-color: green")
self.dlg.Schritt3.setStyleSheet("")
```

---

## Plugin Testen unter

"Processing Toolbox" > "Scripts" (Python Symbol at the top) > "Open Existing Script"

(Can be used to Edit aswell)

In new Window > "Run Script"