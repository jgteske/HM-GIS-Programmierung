# Basic for Loading a Layer in QGIS Python Console
#
# Uebung 03
#

# Remove all Layers
QgsProject.instance().removeAllMapLayers()

uri = "/vsizip/C:/Users/johan/OneDrive/Privat/Uni/Master/02_Semester/GP/Uebung/Week02/natural_earth_vector.gpkg.zip/packages/natural_earth_vector.gpkg|layername=ne_110m_populated_places_simple"
vlayer = iface.addVectorLayer(uri, "places", "ogr")

if vlayer == NULL:
    iface.addVectorLayer(uri, "places", "ogr")
    print("Vector Layer initialized!")


################################################################################
#
# Aufgabe 2 - Heatmap
#

heatmap = QgsHeatmapRenderer()
vlayer.setRenderer(heatmap)
vlayer.triggerRepaint()

heatmap.setRadius(20)
vlayer.setRenderer(heatmap)
vlayer.triggerRepaint()

QgsStyle().defaultStyle().colorRampNames()

#ramp = QgsStyle().defaultStyle().colorRamp('Blues')
ramp = QgsStyle().defaultStyle().colorRamp('Plasma')
heatmap.setColorRamp(ramp)
vlayer.setRenderer(heatmap)
vlayer.triggerRepaint()


# Refresh LayerSymbology
iface.layerTreeView().refreshLayerSymbology(vlayer.id())

