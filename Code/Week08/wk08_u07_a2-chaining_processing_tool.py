my_gpkg = "C:/Users/johan/OneDrive/Privat/Uni/Master/02_Semester/GP/Uebung/Week02/natural_earth_vector.gpkg"
rivers = "{}|layername=ne_110m_rivers_lake_centerlines".format(my_gpkg)
places = "{}|layername=ne_110m_populated_places".format(my_gpkg)

expression = "name = 'Donau'"
danube = processing.run(
    "native:extractbyexpression",
    {"INPUT": rivers, "EXPRESSION": expression, "OUTPUT": "memory:"},
)["OUTPUT"]
buffer_distance = 0.1  # degrees

buffered_danube = processing.run(
    "native:buffer",
    {
        "INPUT": danube,
        "DISTANCE": buffer_distance,
        "SEGMENTS": 5,
        "END_CAP_STYLE": 0,
        "JOIN_STYLE": 0,
        "MITER_LIMIT": 2,
        "DISSOLVE": False,
        "OUTPUT": "memory:",
    },
)["OUTPUT"]

places_along_danube = processing.run(
    "native:extractbylocation",
    {
        "INPUT": places,
        "PREDICATE": [0],
        "INTERSECT": buffered_danube,
        "OUTPUT": "memory:",
    },
)["OUTPUT"]

QgsProject.instance().addMapLayer(places_along_danube)
for feature in places_along_danube.getFeatures():
    print(feature["name"])
