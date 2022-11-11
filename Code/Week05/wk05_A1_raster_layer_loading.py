# Basic for Loading a Layer in QGIS Python Console
#
# Uebung 03
#
# LINKS:
# https://github.com/isogeo/isogeo-plugin-qgis/blob/master/tests/dev/qgis_console/dev_wmts.py

from urllib.parse import unquote, urlencode


# Remove all Layers
QgsProject.instance().removeAllMapLayers()


################################################################################
#
# Aufgabe 1 - Rasterlayer laden und Eigenschaften auslesen
#

# Function to output all information for a QGIS Raster Layer Object
def printInfo(QGISLayer):
    # Info Outputs
    print("\n")
    print(f"Information für den Layer {QGISLayer}:")
    print("Größe des Rasters in Pixel:")
    print(QGISLayer.width(), QGISLayer.height())
    print("Größe des Rasters in Geokoordinaten:")
    print(QGISLayer.extent())
    print(QGISLayer.extent().toString())
    print("Anzahl der Bänder:")
    print(QGISLayer.bandCount())
    print("Bezeichnungen der Bänder:")
    for i in range(1, QGISLayer.bandCount()):
        print("Band Nr. " + str(i) + ": " + QGISLayer.bandName(i))

    print("Min./Max. Werte der Bänder:")
    for i in range(1, QGISLayer.bandCount()):
        stats = QGISLayer.dataProvider().bandStatistics(i)
        print("Band Nr. " + str(i) + ": " + QGISLayer.bandName(i))
        print("Min. Wert: " + str(stats.minimumValue))
        print("Max. Wert: " + str(stats.maximumValue))

    print("Raster Type: ")
    print(QGISLayer.rasterType())
    print("Gesamte Metadata: ")
    print(QGISLayer.metadata())


#
# WMTS
# Services: http://gis.sinica.edu.tw/worldmap/
osmWMTS = (
    "url=http://a.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png&zmax=19&zmin=0&type=xyz"
)
wmtsSettings = {
    "SERVICE": "WMTS",
    "VERSION": "1.0.0",
    "REQUEST": "GetTile",
    "layers": "Topografisk norgeskart 4",
    "crs": "EPSG:4326",
    "format": "image/png",
    "styles": "",
    "tileMatrixSet": "EPSG:4326",
    "url": "http://opencache.statkart.no/gatekeeper/gk/gk.open_wmts?",
}

wmts_url_final = unquote(urlencode(wmtsSettings))
print(wmts_url_final)

# osmWMTS = f'url={wmtsSettings["url"]}&l={wmtsSettings["basename"]}&s=worldmap'

# load Layer
osm_wmts_layer = QgsRasterLayer(osmWMTS, "OSM WMTS", "wms")
print(osm_wmts_layer)
if not osm_wmts_layer.isValid():
    print("Layer osm_wmts_layer failed to load!")
QgsProject.instance().addMapLayer(osm_wmts_layer)


#
# Raster Image TIFF
#
rasterPath = "C:/Users/johan/OneDrive/Privat/Uni/Master/02_Semester/GP/Uebung/Week05/data/rasterStack_b2345_crop.tif"
# iface.addRasterLayer(rasterPath, "RasterImage01")
tifLayer = QgsRasterLayer(rasterPath, "RasterImage01")
if not tifLayer.isValid():
    print("Layer QGISLayer failed to load!")
QgsProject.instance().addMapLayer(tifLayer)

printInfo(tifLayer)


#
# WMS
#
urlWMS = "https://sedac.ciesin.columbia.edu/geoserver/ows?SERVICE=WMS&REQUEST=GetMap&VERSION=1.3.0&layers=ipcc:ipcc-synthetic-vulnerability-climate-2005-2050-2100&format=image/png&crs=EPSG:4326&style=ipcc-synthetic-vulnerability-climate-2005-2050-2100:extreme-events-enhance-adaptive-a2550-2100-5.5C-annual&WIDTH=1500&HEIGHT=800&BBOX=-55.79166793823248,-179.99999966763818,83.66666412494413,179.99999966763812"
WMSSettings = {
    "BASEURL": "https://sedac.ciesin.columbia.edu/geoserver/ows?",
    "SERVICE": "WMS",
    "REQUEST": "GetMap",
    "VERSION": "1.3.0",
    "LAYERS": "ipcc:ipcc-synthetic-vulnerability-climate-2005-2050-2100",
    "FORMAT": "image/png",
    "CRS": "EPSG:4326",
    "STYLE": "ipcc-synthetic-vulnerability-climate-2005-2050-2100:extreme-events-enhance-adaptive-a2550-2100-5.5C-annual",
    "WIDTH": 1500,
    "HEIGHT": 800,
    "BBOX": {
        "LU-Lat": -55.79166793823248,  # links unten Latitude
        "LU-Lon": -179.99999966763818,  # links unten Longitude
        "RO-Lat": 83.66666412494413,  # rechts oben Latitude
        "RO-Lon": 179.99999966763812,  # rechts oben Longitude
    },
}
urlDynamicWMS = f'{WMSSettings["BASEURL"]}SERVICE={WMSSettings["SERVICE"]}&REQUEST={WMSSettings["REQUEST"]}&VERSION={WMSSettings["VERSION"]}&LAYERS={WMSSettings["LAYERS"]}&FORMAT={WMSSettings["FORMAT"]}&CRS={WMSSettings["CRS"]}&STYLE={WMSSettings["STYLE"]}&WIDTH={WMSSettings["WIDTH"]}&HEIGHT={WMSSettings["HEIGHT"]}&BBOX={WMSSettings["BBOX"]["LU-Lat"]},{WMSSettings["BBOX"]["LU-Lon"]},{WMSSettings["BBOX"]["RO-Lat"]},{WMSSettings["BBOX"]["RO-Lon"]}'
urlSplitDynamicWMS = f'layers={WMSSettings["LAYERS"]}&format={WMSSettings["FORMAT"]}&crs={WMSSettings["CRS"]}&url={WMSSettings["BASEURL"]}service={WMSSettings["SERVICE"]}'

urlWithParams = "crs=EPSG:4326&format=image/png&layers=continents&styles&url=https://demo.mapserver.org/cgi-bin/wms"

# load layer
raster_layer = QgsRasterLayer(urlWithParams, "Climate Vulnerability", "wms")
print({raster_layer})
if not raster_layer.isValid():
    print("Layer raster_layer failed to load!")
QgsProject.instance().addMapLayer(raster_layer)

printInfo(raster_layer)
