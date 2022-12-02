# Uebung 01

# Basic for Loading a Layer in QGIS Python Console
uri = "C:/Users/johan/OneDrive/Privat/Uni/Master/02_Semester/GP/Uebung/Week02/natural_earth_vector.gpkg|layername=ne_10m_admin_0_countries"
iface.addVectorLayer(uri, "countries", "ogr")
