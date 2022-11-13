# Basic for Loading a Layer in QGIS Python Console
#
# Uebung 05
#
# LINKS:
#

from qgis.PyQt.QtCore import QVariant
from qgis.core import (
  QgsGeometry,
  QgsPointXY,
  QgsWkbTypes,
  QgsProject,
  QgsVectorLayer,
)

# Remove all Layers
QgsProject.instance().removeAllMapLayers()


################################################################################
#
# Aufgabe 2 - Geometrien anlegen
#

# Create Polygon Layer with crs
vl = QgsVectorLayer('Polygon?crs=epsg:4326', 'Polygon Layer',"memory")

pr = vl.dataProvider()
pr.addAttributes(
    [
        QgsField("name", QVariant.String),
        QgsField("Area", QVariant.Double),
        QgsField("size", QVariant.Double),
    ]
)
vl.updateFields()

#
# Add a Polygon into the Layer
#

# Create Polygon Points in different ways
vrtcs = []
vrtcs.append(QgsPointXY(396100,8969000))
vrtcs.append(QgsPointXY(396100,8973900))
vrtcs.append(QgsPointXY(397900,8973900))
vrtcs.append(QgsPointXY(397900,8969000))

p_points = [
    QgsPointXY(-123, 49),
    QgsPointXY(-123, 50),
    QgsPointXY(-121, 50),
    QgsPointXY(-121, 49),
]

# Create a polygon from the coordinates
gPolygon = QgsGeometry.fromPolygonXY([p_points])
#gPolygon = QgsGeometry.fromPolygonXY([[QgsPointXY(1, 1),QgsPointXY(2, 2), QgsPointXY(2, 1)]])
#gPolygon = QgsGeometry.fromPolygonXY([vrtcs])


# Create a feature object then put the polygon into the feature
poly = QgsFeature()
if gPolygon.isGeosValid:
    # Info about Polygon
    print(gPolygon)
    print("WBK-Type: " + QgsWkbTypes.displayString(gPolygon.wkbType()))

    poly.setGeometry(gPolygon)
    poly.setAttributes(["Test Polygon", gPolygon.area() , 0.6])
    print(poly.geometry())
    pr.addFeature(poly)

vl.updateExtents()
QgsProject.instance().addMapLayer(vl)

#
# Print Statistics
#
print("Anzahl der Felder:", len(pr.fields()))
print("Anzahl der Merkmale:", pr.featureCount())
e = vl.extent()
print("Ausdehnung:", e.xMinimum(), e.yMinimum(), e.xMaximum(), e.yMaximum())
for f in vl.getFeatures():
    print("Feature:", f.id(), f.attributes(), f.geometry().asPolygon())

vl.startEditing()
my_field_name = "new field"
vl.addAttribute(QgsField(my_field_name, QVariant.String))
vl.updateFields()
for f in vl.getFeatures():
    print("Merkmal:", f.id(), f.attributes(), f.geometry().asPolygon())


my_field_value = "Hello world!"
for f in vl.getFeatures():
    f[my_field_name] = my_field_value
    vl.updateFeature(f)
vl.commitChanges()
for f in vl.getFeatures():
    print("Merkmal:", f.id(), f.attributes(), f.geometry().asPolygon())


iface.vectorLayerTools().stopEditing(vl)

my_field_name = "new field"
my_field_value = "Hello world!"
with edit(vl):
    vl.addAttribute(QgsField(my_field_name, QVariant.String))
    vl.updateFields()
    for f in vl.getFeatures():
        f[my_field_name] = my_field_value
        vl.updateFeature(f)
