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
# Aufgabe 1 – Symbole editieren
#

#vlayer.renderer().symbol().setSize(6)
#vlayer.triggerRepaint()
#
#vlayer.renderer().symbol().setColor(QColor('blue')) 
#vlayer.triggerRepaint()
#
#vlayer.renderer().symbol().symbolLayer(0).setShape(QgsSimpleMarkerSymbolLayerBase.Star)
#vlayer.triggerRepaint()

vlayer.renderer().symbol().setSize(6)
vlayer.renderer().symbol().setColor(QColor('blue')) 
vlayer.renderer().symbol().symbolLayer(0).setShape(QgsSimpleMarkerSymbolLayerBase.Star)
vlayer.triggerRepaint()

# Refresh LayerSymbology
iface.layerTreeView().refreshLayerSymbology(vlayer.id())

