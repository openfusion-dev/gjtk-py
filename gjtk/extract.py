"""Extract GeoJSON objects from other GeoJSON objects."""


def positions_of(geojson):
    """ Find all Positions in a valid GeoJSON object. """
    positions = []
    if geojson["type"] == "Point":
        positions.append(geojson["coordinates"])
    elif geojson["type"] in ["MultiPoint", "LineString"]:
        positions += [position for position in geojson["coordinates"]]
    elif geojson["type"] in ["MultiLineString", "Polygon"]:
        positions += [
            position
            for line_string in geojson["coordinates"]
            for position in line_string
        ]
    elif geojson["type"] == "MultiPolygon":
        positions += [
            position
            for polygon in geojson["coordinates"]
            for line_string in polygon
            for position in line_string
        ]
    elif geojson["type"] == "GeometryCollection":
        for geometry in geojson["geometries"]:
            positions += positions_of(geometry)
    elif geojson["type"] == "Feature":
        positions += positions_of(geojson["geometry"])
    elif geojson["type"] == "FeatureCollection":
        for feature in geojson["features"]:
            positions += positions_of(feature)
    return positions


def features_of(geojson):
    """ Find all Features in a valid GeoJSON object. """
    features = []
    if geojson["type"] == "Feature":
        features.append(geojson)
    elif geojson["type"] == "FeatureCollection":
        features += geojson["features"]
    return features


def geometries_of(geojson):
    """ Find all Geometries in a valid GeoJSON object. """
    geometries = []
    if geojson["type"] in [
            "Point",
            "MultiPoint",
            "LineString",
            "MultiLineString",
            "Polygon",
            "MultiPolygon",
    ]:
        geometries.append(geojson)
    elif geojson["type"] == "GeometryCollection":
        for geometry in geojson["geometries"]:
            geometries += geometries_of(geometry)
    elif geojson["type"] == "Feature":
        geometries += geometries_of(geojson["geometry"])
    elif geojson["type"] == "FeatureCollection":
        for feature in geojson["features"]:
            geometries += geometries_of(feature)
    return geometries
