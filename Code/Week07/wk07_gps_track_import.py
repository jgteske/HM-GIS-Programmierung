import time
import os
from xml.dom import minidom

workingDir = os.getcwd()
# filePath = os.path.join(workingDir,"ride.gpx")
filePath = r"C:\Users\johan\Documents\Studium\Master\Master02\GitHub\HM-GIS-Programmierung\Code\Week07\ride.gpx"

# READ GPX FILE
data = open(filePath)
xmldoc = minidom.parse(data)
track = xmldoc.getElementsByTagName("trkpt")
n_track = len(track)

# PARSING GPX ELEMENT AND CREATING MARKER
marker_list = []
canvas = iface.mapCanvas()
for s in range(n_track):
    lon, lat = track[s].attributes["lon"].value, track[s].attributes["lat"].value
    x = float(lon)
    y = float(lat)
    m = QgsVertexMarker(canvas)
    m.setCenter(QgsPointXY(x, y))
    m.setColor(QColor(255, 0, 0))
    m.setFillColor(QColor(255, 255, 0))
    m.setIconSize(10)
    m.setIconType(QgsVertexMarker.ICON_CIRCLE)
    m.setPenWidth(3)
    marker_list.append(m)
    time.sleep(0.1)
    print(m)


# FUNCTION TO HIDE AND PLAY TRACK ANIMATION
def hide_track():
    for i in range(n_track):
        marker_list[i].hide()


def play_track():
    hide_track()
    for j in range(n_track):
        marker_list[j].show()
        time.sleep(0.1)  # Time interval. You can change it here
        print(marker_list[j])
