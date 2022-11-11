# Basic for Loading a Layer in QGIS Python Console
#
# Uebung 05
#
# LINKS:
#

from qgis.PyQt.QtCore import QVariant

# Remove all Layers
QgsProject.instance().removeAllMapLayers()


################################################################################
#
# Aufgabe 1 - Vektorlayer erzeugen
#

vl = QgsVectorLayer("Point", "temp", "memory")

pr = vl.dataProvider()
pr.addAttributes(
    [
        QgsField("name", QVariant.String),
        QgsField("age", QVariant.Int),
        QgsField("size", QVariant.Double),
    ]
)
vl.updateFields()

f = QgsFeature()
f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(10, 10)))
f.setAttributes(["Ada L.", 2, 0.3])
pr.addFeature(f)
vl.updateExtents()
QgsProject.instance().addMapLayer(vl)


print("Anzahl der Felder:", len(pr.fields()))
print("Anzahl der Merkmale:", pr.featureCount())
e = vl.extent()
print("Ausdehnung:", e.xMinimum(), e.yMinimum(), e.xMaximum(), e.yMaximum())
for f in vl.getFeatures():
    print("Feature:", f.id(), f.attributes(), f.geometry().asPoint())

vl.startEditing()
my_field_name = "new field"
vl.addAttribute(QgsField(my_field_name, QVariant.String))
vl.updateFields()
for f in vl.getFeatures():
    print("Merkmal:", f.id(), f.attributes(), f.geometry().asPoint())


my_field_value = "Hello world!"
for f in vl.getFeatures():
    f[my_field_name] = my_field_value
    vl.updateFeature(f)
vl.commitChanges()
for f in vl.getFeatures():
    print("Merkmal:", f.id(), f.attributes(), f.geometry().asPoint())

iface.vectorLayerTools().stopEditing(vl)

my_field_name = "new field"
my_field_value = "Hello world!"
with edit(vl):
    vl.addAttribute(QgsField(my_field_name, QVariant.String))
    vl.updateFields()
    for f in vl.getFeatures():
        f[my_field_name] = my_field_value
        vl.updateFeature(f)
