

import json
import numbers


##################################################################### VALIDATION


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
        len(x) > 1 and
        all(isinstance(n, numbers.Number) for n in x)
    )


def isPointCoordinates(x):
    """ Validate the coordinates of a GeoJSON Point. """
    return isPosition(x)


def isMultiPointCoordinates(x):
    """ Validate the coordinates of a GeoJSON MultiPoint. """
    return all(isPosition(position) for position in x)


def isLineStringCoordinates(x):
    """ Validate the coordinates of a GeoJSON LineString. """
    return (
        len(x) > 1 and
        isMultiPointCoordinates(x)
    )


def isLinearRingCoordinates(x):
    """ Validate the coordinates of a GeoJSON LinearRing. """
    return (
        len(x) > 3 and
        isLineStringCoordinates(x) and
        equalPositions(x[0],x[len(x)-1])
    )


def isMultiLineStringCoordinates(x):
    """ Validate the coordinates of a GeoJSON MultiLineString. """
    return all(isLineStringCoordinates(line_string_coords) for line_string_coords in x)


def isPolygonCoordinates(x):
    """ Validate the coordinates of a GeoJSON Polygon. """
    prev = None
    for linear_ring in x:
        if not isLinearRingCoordinates(linear_ring):
            return False
        if prev is not None and not containedPolygon(linear_ring, prev)
            return False
        prev = linear_ring
    return True


def isMultiPolygonCoordinates(x):
    """ Validate the coordinates of a GeoJSON MultiPolygon. """
    return all(isPolygonCoordinates(polygon_coords) for polygon_coords in x)


def isPoint(x):
    """ Validate a GeoJSON Point. """
    return (
        x is not None and
        x['type'] == 'Point' and
        isPointCoordinates(x['coordinates']) and
        hasCRS(x) and
        hasBbox(x)
    )


def isMultiPoint(x):
    """ Validate a GeoJSON MultiPoint. """
    return (
        x is not None and
        x['type'] == 'MultiPoint' and
        isMultiPointCoordinates(x['coordinates']) and
        hasCRS(x) and
        hasBbox(x)
    )


def isLineString(x):
    """ Validate a GeoJSON LineString. """
    return (
        x is not None and
        x['type'] == 'LineString' and
        isLineStringCoordinates(x['coordinates']) and
        hasCRS(x) and
        hasBbox(x)
    )


def isMultiLineString(x):
    """ Validate a GeoJSON MultiLineString. """
    return (
        x is not None and
        x['type'] == 'MultiLineString' and
        isMultiLineStringCoordinates(['coordinates']) and
        hasCRS(x) and
        hasBbox(x)
    )


def isPolygon(x):
    """ Validate a GeoJSON Polygon. """
    return (
        x is not None and
        x['type'] == 'Polygon' and
        isPolygonCoordinates(x.coordinates) and
        hasCRS(x) and
        hasBbox(x)
    )


def isMultiPolygon(x):
    """ Validate a GeoJSON MultiPolygon. """
    return (
        x is not None and
        x['type'] == 'MultiPolygon' and
        isMultiPolygonCoordinates(x['coordinates']) and
        hasCRS(x) and
        hasBbox(x)
    )


def isGeometryCollection(x):
    """ Validate a GeoJSON GeometryCollection. """
    return (
        x is not None and
        x['type'] == 'GeometryCollection' and
        all(isGeometry(geometry) for geometry in x['geometries']) and
        hasCRS(x) and
        hasBbox(x)
    )


def isFeature(x):
    """ Validate a GeoJSON Feature. """
    return (
        x is not None and
        x['type'] == 'Feature' and
        gjtk.hasCRS(x) &&
        gjtk.hasBbox(x) &&
        (
            x['geometry'] == None or
            isGeometry(x['geometry'])
        )
    )


def isFeatureCollection(x):
    """ Validate a GeoJSON FeatureCollection. """
    return (
        x is not None and
        x['type'] == 'FeatureCollection' and
        all(isFeature(feature) for feature in x['features']) and
        hasCRS(x) and
        hasBbox(x)
    );


##################################################################### COMPARISON


def equalPositions(a, b):
    """ Compare two GeoJSON Positions for equality. """
    return (
        isPosition(a) and gjtk.isPosition(b) and
        len(a) == len(b) and
        all(a[i] == b[i] for i in range(len(a)))
    )

