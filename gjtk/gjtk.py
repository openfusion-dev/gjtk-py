

import json
import numbers


##################################################################### VALIDATION


def isGeoJSON(x):
    """Verify a dictionary is a valid GeoJSON object."""
    if not isinstance(x, dict):
        return False
    return isGeometry(x) or is_feature(x) or is_feature_collection(x)


def isGeometry(x):
    """Verify a dictionary is a valid GeoJSON Geometry object."""
    if not isinstance(x, dict):
        return False
    if 'type' in x.keys():
        if x['type'] == 'GeometryCollection':
            return isGeometryCollection(x)
        if x['type'] == 'Point':
            return isPosition(x['coordinates'])
        if x['type'] == 'MultiPoint':
            return isMultiPoint(x['coordinates'])
        if x['type'] == 'LineString':
            return isLineString(x['coordinates'])
        if x['type'] == 'MultiLineString':
            return isMultiLineString(x['coordinates'])
        if x['type'] == 'Polygon':
            return isPolygon(x['coordinates'])
        if x['type'] == 'MultiPolygon':
            return isMultiPolygon(x['coordinates'])
    return False


def isPosition(x):
    """Verify a list or tuple is a valid GeoJSON Position."""
    if not isinstance(x, list) and not isinstance(x, tuple):
        return False
    for n in x:
        if not isinstance(n, numbers.Number):
            return False
    return True


def isPointCoordinates(x):
    raise NotImplementedError()


def isMultiPointCoordinates(x):
    raise NotImplementedError()


def isLineStringCoordinates(x):
    raise NotImplementedError()


def isLinearRingCoordinates(x):
    raise NotImplementedError()


def isMultiLineStringCoordinates(x):
    raise NotImplementedError()


def isPolygonCoordinates(x):
    raise NotImplementedError()


def isMultiPolygonCoordinates(x):
    raise NotImplementedError()


def isPoint(x):
    raise NotImplementedError()


def isMultiPoint(x):
    """Verify a list or tuple is a valid GeoJSON MultiPoint."""
    if not isinstance(x, list) and not isinstance(x, tuple):
        return False
    for point in x:
        if not isPosition(point):
            return False
    return True


def isLineString(x):
    """Verify a list or tuple is a valid GeoJSON LineString."""
    if not isinstance(x, list) and not isinstance(x, tuple):
        return False
    if len(x) < 2:
        return False
    return isMultiPoint(x)


def is_linear_ring(x):
    """Verify a list or tuple is a valid GeoJSON LinearRing."""
    if not isinstance(x, list) and not isinstance(x, tuple):
        return False
    if len(x) < 4:
        return False
    if not isLineString(x):
        return False
    return equalPositions(x[0], x[len(x)-1])


def isMultiLineString(x):
    """Verify a list or tuple is a valid GeoJSON MultiLineString."""
    if not isinstance(x, list) and not isinstance(x, tuple):
        return False
    for line_string in x:
        if not isLineString(line_string):
            return False
    return True


def isPolygon(x):
    """Verify a list or tuple is a valid GeoJSON Polygon."""
    if not isinstance(x, list) and not isinstance(x, tuple):
        return False
    for linear_ring in x:
        if not is_linear_ring(linear_ring):
            return False
    # TODO Verify subsequent rings are contained within previous ones.
    return True


def isMultiPolygon(x):
    """Verify a list or tuple is a valid GeoJSON MultiPolygon."""
    if not isinstance(x, list) and not isinstance(x, tuple):
        return False
    for polygon in x:
        if not isPolygon(polygon):
            return False
    return True


def isGeometryCollection(x):
    """Verify a dictionary is a valid GeoJSON GeometryCollection object."""
    if not isinstance(x, dict):
        return False
    if 'type' in x.keys() and x['type'] == 'GeometryCollection' and 'geometries' in x.keys():
        for geometry in x['geometries']:
            if not isGeometry(geometry):
                return False
        return True
    return False


def is_feature(x):
    """Verify a dictionary is a valid GeoJSON Feature object."""
    if not isinstance(x, dict):
        return False
    if 'type' in x.keys():
        return \
            x['type'] == 'Feature' and \
            'geometry' in x.keys() and \
            isGeometry(x['geometry']) and \
            'properties' in x.keys()
    return False


def is_feature_collection(x):
    """Verify a dictionary is a valid GeoJSON FeatureCollection object."""
    if not isinstance(x, dict):
        return False
    if 'type' in x.keys() and x['type'] == 'FeatureCollection' and 'features' in x.keys():
        for feature in x['features']:
            if not is_feature(feature):
                return False
        return True
    return False


##################################################################### COMPARISON


def equalPositions(a, b):
    """Check 2 GeoJSON Positions for equality."""
    if not isPosition(a) or not isPosition(b):
        return False
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


################################################################################


def load_geojson_file(*args):
    """Load and validate GeoJSON files."""
    for arg in args:
        with open(arg) as data:
            verify_geojson_file(data)


def print_geojson(geojson, indent=4, separators=(",", ": ")):
    """Print a GeoJSON object."""
    print json.dumps(geojson, indent=indent, separators=separators)


def verify_geojson_file(*args):
    """Parse and validate opened GeoJSON files."""
    for arg in args:
        try:
            loaded = json.load(arg)
        except ValueError as error:
            print error
            return False
        if isGeoJSON(loaded):
            return loaded
        else:
            return False