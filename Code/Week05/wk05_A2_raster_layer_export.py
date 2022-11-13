# Basic for Loading a Layer in QGIS Python Console
#
# Uebung 03
#
# LINKS:
# https://data.library.virginia.edu/how-to-create-and-export-print-layouts-in-python-for-qgis-3/

import os

################################################################################
#
# Aufgabe 2 – Ein Layer in ein pdf exportieren
#

# Define Variables
exportPath = 'C:/Users/johan/OneDrive/Privat/Uni/Master/02_Semester/GP/Uebung/Week05/data/qgis_export/'
exportName = 'test_export'
exportType = '.pdf'
fileName = exportName+exportType

exportFile = os.path.join(exportPath + fileName)
print("Speicherort: " + exportFile)
quickExportFile = os.path.join(exportPath, f'{exportName}.png')
print("Quickexport Speicherort: " + quickExportFile)

#
# Create Layout
#
layoutName = "PrintLayout"
project = QgsProject.instance()
manager = project.layoutManager()

# recreate PrintLayout
layouts_list = manager.printLayouts()
print(layouts_list)
for layout in layouts_list:
    if layout.name() == layoutName:
        manager.removeLayout(layout)

layout = QgsPrintLayout(project)
#initializes default settings for blank print layout canvas
layout.initializeDefaults()
layout.setName(layoutName)
manager.addLayout(layout)


#
# Adding Layout-Items to the layout
#

#
# Map extend
map = QgsLayoutItemMap(layout)
map.setRect(20, 20, 20, 20)

#Set Map Extent
#defines map extent using map coordinates
#rectangle = QgsRectangle(1355502, -46398, 1734534, 137094)
#map.setExtent(rectangle)
#layout.addLayoutItem(map)
canvas = iface.mapCanvas()
map.setExtent(canvas.extent())

#Move & Resize map on print layout canvas
map.attemptMove(QgsLayoutPoint(5, 27, QgsUnitTypes.LayoutMillimeters))
map.attemptResize(QgsLayoutSize(239, 178, QgsUnitTypes.LayoutMillimeters))

layout.addLayoutItem(map)


#
# Legend
#Checks layer tree objects and stores them in a list. This includes csv tables
checked_layers = [layer.name() for layer in QgsProject().instance().layerTreeRoot().children() if layer.isVisible()]
print(f"Adding {checked_layers} to legend." )
#get map layer objects of checked layers by matching their names and store those in a list
layersToAdd = [layer for layer in QgsProject().instance().mapLayers().values() if layer.name() in checked_layers]

legend = QgsLayoutItemLegend(layout)
legend.setTitle("Legende:")
root = QgsLayerTree()
for layer in layersToAdd:
    #add layer objects to the layer tree
    root.addLayer(layer)
legend.model().setRootGroup(root)
layout.addLayoutItem(legend)
legend.attemptMove(QgsLayoutPoint(246, 5, QgsUnitTypes.LayoutMillimeters))

#
# Title
title = QgsLayoutItemLabel(layout)
title.setText("Aufgabe2")
title.setFont(QFont("Arial", 25))
title.adjustSizeToText()
layout.addLayoutItem(title)
title.attemptMove(QgsLayoutPoint(10, 4, QgsUnitTypes.LayoutMillimeters))

subtitle = QgsLayoutItemLabel(layout)
subtitle.setText("Ein Layer in ein pdf exportieren")
subtitle.setFont(QFont("Arial", 17))
subtitle.adjustSizeToText()
layout.addLayoutItem(subtitle)
subtitle.attemptMove(QgsLayoutPoint(11, 20, QgsUnitTypes.LayoutMillimeters))   #allows moving text box

#
# Scale Bars
item = QgsLayoutItemScaleBar(layout)
item.setStyle('Numeric') # optionally modify the style
item.setLinkedMap(map) # map is an instance of QgsLayoutItemMap
item.applyDefaultSize()
layout.addLayoutItem(item)
item.setAlignment(0) # AlignLeft = 0; AlignMiddle = 1; AlignRight = 2
item.attemptMove(QgsLayoutPoint(246, 200, QgsUnitTypes.LayoutMillimeters))   #allows moving text box

#
# Random Polygons
""" polygon = QPolygonF()
polygon.append(QPointF(0.0, 0.0))
polygon.append(QPointF(100.0, 0.0))
polygon.append(QPointF(200.0, 100.0))
polygon.append(QPointF(100.0, 200.0))
polygonItem = QgsLayoutItemPolygon(polygon, layout)
layout.addLayoutItem(polygonItem)
props = {}
props["color"] = "green"
props["style"] = "solid"
props["style_border"] = "solid"
props["color_border"] = "black"
props["width_border"] = "10.0"
props["joinstyle"] = "miter"
symbol = QgsFillSymbol.createSimple(props)
polygonItem.setSymbol(symbol) """


#
# Start Exporting Process
#
print('Available PrintLayouts: ')
for layout in manager.printLayouts():
    print(layout.name())

layout = manager.layoutByName(layoutName)

exporter = QgsLayoutExporter(layout)
exporter.exportToPdf(exportFile, QgsLayoutExporter.PdfExportSettings())

# schneller Export der aktuellen Karte
iface.mapCanvas().saveAsImage(quickExportFile)