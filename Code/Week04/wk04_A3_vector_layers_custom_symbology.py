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
# Aufgabe 3 - Datendefinierte Symbolgröße
#

exp = 'scale_linear("pop_max", 0, 10000000, 0, 7)'
renderer = vlayer.renderer().clone()
renderer.symbol().symbolLayer(0).setDataDefinedProperty(QgsSymbolLayer.PropertySize, QgsProperty.fromExpression(exp) )
vlayer.setRenderer(renderer)


vlayer.triggerRepaint()

# Refresh LayerSymbology
iface.layerTreeView().refreshLayerSymbology(vlayer.id())
vlayer.reload()

