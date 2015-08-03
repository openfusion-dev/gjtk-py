

from matplotlib.path import Path
from numbers import Number


def isGeoJSON(x):
    """ Validate a GeoJSON object. """
    return (
        isGeometry(x) or
        isFeature(x) or
        isFeatureCollection(x)
    )


def isGeometry(x):
    """ Validate a GeoJSON Geometry. """
    return (
        isPoint(x) or
        isMultiPoint(x) or
        isLineString(x) or
        isMultiLineString(x) or
        isPolygon(x) or
        isMultiPolygon(x) or
        isGeometryCollection(x)
    )


def isPosition(x):
    """ Validate a GeoJSON Position. """
    return (
        x is not None and
        len(x) > 1 and
        all(isinstance(n, Number) for n in x)
    )


def isPointCoordinates(x):
    """ Validate the coordinates of a GeoJSON Point. """
    return isPosition(x)


def isMultiPointCoordinates(x):
    """ Validate the coordinates of a GeoJSON MultiPoint. """
    return x is not None and all(isPosition(position) for position in x)


def isLineStringCoordinates(x):
    """ Validate the coordinates of a GeoJSON LineString. """
    return (
        x is not None and
        len(x) > 1 and
        all(isPosition(position) for position in x)
    )


def isLinearRingCoordinates(x):
    """ Validate the coordinates of a GeoJSON LinearRing. """
    return (
        x is not None and
        len(x) > 3 and
        isLineStringCoordinates(x) and
        equalPositions(x[0],x[len(x)-1])
    )


def isMultiLineStringCoordinates(x):
    """ Validate the coordinates of a GeoJSON MultiLineString. """
    return x is not None and all(isLineStringCoordinates(line_string_coords) for line_string_coords in x)


def isPolygonCoordinates(x):
    """ Validate the coordinates of a GeoJSON Polygon. """
    if x is None:
        return False
    prev = None
    for linear_ring in x:
        if not isLinearRingCoordinates(linear_ring):
            return False
        if prev is not None and not containedPolygon(linear_ring, prev):
            return False
        prev = linear_ring
    return True


def isMultiPolygonCoordinates(x):
    """ Validate the coordinates of a GeoJSON MultiPolygon. """
    return x is not None and all(isPolygonCoordinates(polygon_coords) for polygon_coords in x)


def isPoint(x):
    """ Validate a GeoJSON Point. """
    return (
        x is not None and
        x.get("type") == "Point" and
        isPointCoordinates(x.get("coordinates")) and
        hasCRS(x) and
        hasBbox(x)
    )


def isMultiPoint(x):
    """ Validate a GeoJSON MultiPoint. """
    return (
        x is not None and
        x.get("type") == "MultiPoint" and
        isMultiPointCoordinates(x.get("coordinates")) and
        hasCRS(x) and
        hasBbox(x)
    )


def isLineString(x):
    """ Validate a GeoJSON LineString. """
    return (
        x is not None and
        x.get("type") == "LineString" and
        isLineStringCoordinates(x.get("coordinates")) and
        hasCRS(x) and
        hasBbox(x)
    )


def isMultiLineString(x):
    """ Validate a GeoJSON MultiLineString. """
    return (
        x is not None and
        x.get("type") == "MultiLineString" and
        isMultiLineStringCoordinates(x.get("coordinates")) and
        hasCRS(x) and
        hasBbox(x)
    )


def isPolygon(x):
    """ Validate a GeoJSON Polygon. """
    return (
        x is not None and
        x.get("type") == "Polygon" and
        isPolygonCoordinates(x.get("coordinates")) and
        hasCRS(x) and
        hasBbox(x)
    )


def isMultiPolygon(x):
    """ Validate a GeoJSON MultiPolygon. """
    return (
        x is not None and
        x.get("type") == "MultiPolygon" and
        isMultiPolygonCoordinates(x.get("coordinates")) and
        hasCRS(x) and
        hasBbox(x)
    )


def isGeometryCollection(x):
    """ Validate a GeoJSON GeometryCollection. """
    return (
        x is not None and
        x.get("type") == "GeometryCollection" and
        x.has_key("geometries") and
        all(isGeometry(geometry) for geometry in x["geometries"]) and
        hasCRS(x) and
        hasBbox(x)
    )


def isFeature(x):
    """ Validate a GeoJSON Feature. """
    return (
        x is not None and
        x.get("type") == "Feature" and
        x.has_key("geometry") and
        (
            x["geometry"] is None or
            isGeometry(x["geometry"])
        ) and
        hasCRS(x) and
        hasBbox(x)
    )


def isFeatureCollection(x):
    """ Validate a GeoJSON FeatureCollection. """
    return (
        x is not None and
        x.get("type") == "FeatureCollection" and
        x.has_key("features") and
        all(isFeature(feature) for feature in x.get("features")) and
        hasCRS(x) and
        hasBbox(x)
    );


def isCRS(x):
    """ Validate a GeoJSON Coordinate Reference System. """
    return (
        x is not None and
        (
            (
                x.get("type") == "name" and
                x.get("properties") is not None and
                len(str(x["properties"].get("name", ""))) > 0
            ) or
            (
                x.get("type") == "link" and
                isLink(x.get("properties"))
            )
        )
    )


def hasCRS(x):
    """ Validate the CRS property of a GeoJSON object. """
    return (
        x is not None and
        (
            x.get("crs") is None or
            isCRS(x["crs"])
        )
    )


def isLink(x):
    """ Validate a GeoJSON Link. """
    try:
        return (
            x is not None and
            (
                x.get("type") is None or
                len(str(x["type"])) > 0
            ) and
            str(x["href"])
        )
    except:
        return False


def isBbox(x):
    """ Validate a GeoJSON Bounding Box. """
    if x is None or len(x)%2 != 0:
        return False
    pivot = len(x)/2
    for i in range(pivot):
        if x[i] > x[i+pivot]:
            return False
    return True


def hasBbox(x):
    """ Validate the bbox property of a GeoJSON object. """
    return (
        x is not None and
        (
            x.get("bbox") is None or
            isBbox(x["bbox"])
        )
    )


##################################################################### COMPARISON


def equalPositions(a, b):
    """ Compare two GeoJSON Positions for equality. """
    return (
        isPosition(a) and isPosition(b) and
        len(a) == len(b) and
        all(a[i] == b[i] for i in range(len(a)))
    )


def containedPolygon(inner, outer):
    """ Determine whether one GeoJSON LinearRing contains another. """
    outer_path = Path(outer)
    return all(outer_path.contains_point([position[0], position[1]]) for position in inner)


##################################################################### DEPRECATED


def validCRS(x):
    """ DEPRECATED: Use hasCRS instead. """
    return hasCRS(x)


def validBbox(x):
    """ DEPRECATED: Use hasBbox instead. """
    return hasBbox(x)

