

from matplotlib.path import Path
from numbers import Number


def boolean_fail(f):
    def wrapped_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return False
    return wrapped_f


@boolean_fail
def isGeoJSON(anything):
    """ Validate a GeoJSON object. """
    return (
        isGeometry(anything) or
        isFeature(anything) or
        isFeatureCollection(anything)
    )


@boolean_fail
def isGeometry(anything):
    """ Validate a GeoJSON Geometry. """
    return (
        isPoint(anything) or
        isMultiPoint(anything) or
        isLineString(anything) or
        isMultiLineString(anything) or
        isPolygon(anything) or
        isMultiPolygon(anything) or
        isGeometryCollection(anything)
    )


@boolean_fail
def isPosition(anything):
    """ Validate a GeoJSON Position. """
    return (
        anything is not None and
        len(anything) > 1 and
        all(isinstance(n, Number) for n in anything)
    )


@boolean_fail
def isPointCoordinates(anything):
    """ Validate the coordinates of a GeoJSON Point. """
    return isPosition(anything)


@boolean_fail
def isMultiPointCoordinates(anything):
    """ Validate the coordinates of a GeoJSON MultiPoint. """
    return anything is not None and all(isPosition(position) for position in anything)


@boolean_fail
def isLineStringCoordinates(anything):
    """ Validate the coordinates of a GeoJSON LineString. """
    return (
        anything is not None and
        len(anything) > 1 and
        all(isPosition(position) for position in anything)
    )


@boolean_fail
def isLinearRingCoordinates(anything):
    """ Validate a GeoJSON LinearRing. """
    return (
        anything is not None and
        len(anything) > 3 and
        isLineStringCoordinates(anything) and
        equalPositions(anything[0],anything[len(anything)-1])
    )


@boolean_fail
def isMultiLineStringCoordinates(anything):
    """ Validate the coordinates of a GeoJSON MultiLineString. """
    return anything is not None and all(isLineStringCoordinates(line_string_coords) for line_string_coords in anything)


@boolean_fail
def isPolygonCoordinates(anything):
    """ Validate the coordinates of a GeoJSON Polygon. """
    if anything is None:
        return False
    prev = None
    for linear_ring in anything:
        if not isLinearRingCoordinates(linear_ring):
            return False
        if prev is not None and not containedPolygon(linear_ring, prev):
            return False
        prev = linear_ring
    return True


@boolean_fail
def isMultiPolygonCoordinates(anything):
    """ Validate the coordinates of a GeoJSON MultiPolygon. """
    return anything is not None and all(isPolygonCoordinates(polygon_coords) for polygon_coords in anything)


@boolean_fail
def isPoint(anything):
    """ Validate a GeoJSON Point. """
    return (
        anything is not None and
        anything.get("type") == "Point" and
        isPointCoordinates(anything.get("coordinates")) and
        hasCRS(anything) and
        hasBbox(anything)
    )


@boolean_fail
def isMultiPoint(anything):
    """ Validate a GeoJSON MultiPoint. """
    return (
        anything is not None and
        anything.get("type") == "MultiPoint" and
        isMultiPointCoordinates(anything.get("coordinates")) and
        hasCRS(anything) and
        hasBbox(anything)
    )


@boolean_fail
def isLineString(anything):
    """ Validate a GeoJSON LineString. """
    return (
        anything is not None and
        anything.get("type") == "LineString" and
        isLineStringCoordinates(anything.get("coordinates")) and
        hasCRS(anything) and
        hasBbox(anything)
    )


@boolean_fail
def isMultiLineString(anything):
    """ Validate a GeoJSON MultiLineString. """
    return (
        anything is not None and
        anything.get("type") == "MultiLineString" and
        isMultiLineStringCoordinates(anything.get("coordinates")) and
        hasCRS(anything) and
        hasBbox(anything)
    )


@boolean_fail
def isPolygon(anything):
    """ Validate a GeoJSON Polygon. """
    return (
        anything is not None and
        anything.get("type") == "Polygon" and
        isPolygonCoordinates(anything.get("coordinates")) and
        hasCRS(anything) and
        hasBbox(anything)
    )


@boolean_fail
def isMultiPolygon(anything):
    """ Validate a GeoJSON MultiPolygon. """
    return (
        anything is not None and
        anything.get("type") == "MultiPolygon" and
        isMultiPolygonCoordinates(anything.get("coordinates")) and
        hasCRS(anything) and
        hasBbox(anything)
    )


@boolean_fail
def isGeometryCollection(anything):
    """ Validate a GeoJSON GeometryCollection. """
    return (
        anything is not None and
        anything.get("type") == "GeometryCollection" and
        anything.has_key("geometries") and
        all(isGeometry(geometry) for geometry in anything["geometries"]) and
        hasCRS(anything) and
        hasBbox(anything)
    )


@boolean_fail
def isFeature(anything):
    """ Validate a GeoJSON Feature. """
    return (
        anything is not None and
        anything.get("type") == "Feature" and
        anything.has_key("geometry") and
        (
            anything["geometry"] is None or
            isGeometry(anything["geometry"])
        ) and
        hasCRS(anything) and
        hasBbox(anything)
    )


@boolean_fail
def isFeatureCollection(anything):
    """ Validate a GeoJSON FeatureCollection. """
    return (
        anything is not None and
        anything.get("type") == "FeatureCollection" and
        anything.has_key("features") and
        all(isFeature(feature) for feature in anything.get("features")) and
        hasCRS(anything) and
        hasBbox(anything)
    );


@boolean_fail
def isCRS(anything):
    """ Validate a GeoJSON Coordinate Reference System. """
    return (
        anything is not None and
        (
            (
                anything.get("type") == "name" and
                anything.get("properties") is not None and
                len(str(anything["properties"].get("name", ""))) > 0
            ) or
            (
                anything.get("type") == "link" and
                isLink(anything.get("properties"))
            )
        )
    )


@boolean_fail
def hasCRS(anything):
    """ Validate the crs property of a GeoJSON object. """
    return (
        anything is not None and
        (
            anything.get("crs") is None or
            isCRS(anything["crs"])
        )
    )


@boolean_fail
def isLink(anything):
    """ Validate a GeoJSON Link. """
    try:
        return (
            anything is not None and
            (
                anything.get("type") is None or
                len(str(anything["type"])) > 0
            ) and
            str(anything["href"])
        )
    except:
        return False


@boolean_fail
def isBbox(anything):
    """ Validate a GeoJSON Bounding Boanything. """
    if anything is None or len(anything)%2 != 0:
        return False
    pivot = len(anything)/2
    for i in range(pivot):
        if anything[i] > anything[i+pivot]:
            return False
    return True


@boolean_fail
def hasBbox(anything):
    """ Validate the bbox property of a GeoJSON object. """
    return (
        anything is not None and
        (
            anything.get("bbox") is None or
            isBbox(anything["bbox"])
        )
    )


##################################################################### COMPARISON


@boolean_fail
def equalPositions(a, b):
    """ Compare two GeoJSON Positions for equality. """
    return (
        isPosition(a) and isPosition(b) and
        len(a) == len(b) and
        all(a[i] == b[i] for i in range(len(a)))
    )


@boolean_fail
def containedPolygon(inner, outer):
    """ Determine whether one GeoJSON LinearRing contains another. """
    outer_path = Path(outer)
    return all(outer_path.contains_point([position[0], position[1]]) for position in inner)


##################################################################### DEPRECATED


@boolean_fail
def validCRS(anything):
    """ DEPRECATED: Use hasCRS instead. """
    return hasCRS(anything)


@boolean_fail
def validBbox(anything):
    """ DEPRECATED: Use hasBbox instead. """
    return hasBbox(anything)

