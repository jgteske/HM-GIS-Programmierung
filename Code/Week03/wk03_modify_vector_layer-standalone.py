# Basic for Loading a Layer in QGIS Python Console
#
# Uebung 02
#
# https://docs.qgis.org/2.18/en/docs/pyqgis_developer_cookbook/intro.html#using-pyqgis-in-standalone-scripts
# Code documentation:
# https://docs.qgis.org/2.18/en/docs/pyqgis_developer_cookbook/index.html

# Base Imports done in qgis internal console
from qgis.core import *
import qgis.utils

# More Imports


# supply path to qgis install location
QgsApplication.setPrefixPath("C:\Program Files\QGIS 3.26.3\bin", True)

# create a reference to the QgsApplication, setting the
# second argument to False disables the GUI
qgs = QgsApplication([], False)

# load providers
qgs.initQgis()


# path to files
uri="/vsizip/C:/Users/johan/OneDrive/Privat/Uni/Master/02_Semester/GP/Uebung/Week02/natural_earth_vector.gpkg.zip/packages/natural_earth_vector.gpkg|layername=ne_10m_admin_0_countries"

layer = iface.activeLayer()
print(layer)

if layer == NULL:
    iface.addVectorLayer(uri, "countries", "ogr")
    print("Vector Layer initialized!")

# Display Attributes of Layer
iface.showAttributeTable(layer)

# Print Fields of Layer (Fieldnames)
for field in layer.fields():
    print(field.name())

for feature in layer.getFeatures():
    print(feature["ADMIN"])

# Filtered
layer.setSubsetString("ADMIN LIKE 'A%'")
for feature in layer.getFeatures():
    print(feature["ADMIN"])

# No Filter
layer.setSubsetString("")
for feature in layer.getFeatures():
    print(feature["ADMIN"])

my_char = "C"
layer.setSubsetString("ADMIN LIKE '"+my_char+"%'")
print("Die folgenden Ländernamen beginnen mit {}:".format(my_char))
for feature in layer.getFeatures():
    print(feature['ADMIN'])

for feature in layer.getFeatures():
    print("{pop:.2f} Mio Menschen leben in {name}".format(name=feature['ADMIN'],pop=feature['POP_EST']/1000000))


# When your script is complete, call exitQgis() to remove the provider and
# layer registries from memory
qgs.exitQgis()