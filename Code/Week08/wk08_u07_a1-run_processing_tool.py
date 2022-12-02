uri = "C:/Users/johan/OneDrive/Privat/Uni/Master/02_Semester/GP/Uebung/Week02/natural_earth_vector.gpkg|layername=ne_110m_populated_places"

result = processing.run(
    "native:buffer",
    {
        "INPUT": uri,
        "DISTANCE": 8,
        "SEGMENTS": 5,
        "END_CAP_STYLE": 0,
        "JOIN_STYLE": 0,
        "MITER_LIMIT": 2,
        "DISSOLVE": False,
        "OUTPUT": "memory:",
    },
)

QgsProject.instance().addMapLayer(result["OUTPUT"])

processing.runAndLoadResults("native:buffer",
{'INPUT':uri,'DISTANCE':10,'SEGMENTS':5,'END_CAP_STYLE':0,'JOIN_STYLE':0,'MITER_LIMIT':2,'DISSOLVE':False,'OUTPUT':'memory:'})
