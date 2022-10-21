# Basic for Loading a Layer in QGIS Python Console
uri="/vsizip/C:/Users/johan/OneDrive/Privat/Uni/Master/02_Semester/GP/Uebung/Week02/natural_earth_vector.gpkg.zip/packages/natural_earth_vector.gpkg|layername=ne_10m_admin_0_countries"
iface.addVectorLayer(uri, "countries", "ogr")
print("Vector Layer initialized!")

iface.showAttributeTable(vlayer)