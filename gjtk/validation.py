"""GeoJSON Validator"""

# TODO Validate CRS objects.
# TODO Validate bbox members.

import numbers


def equal_positions(a, b):
    """Check 2 GeoJSON Positions for equality."""
    if not is_position(a) or not is_position(b):
        return False
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


def is_position(x):
    """Verify a list or tuple is a valid GeoJSON Position."""
    if not isinstance(x, list) and not isinstance(x, tuple):
        return False
    for n in x:
        if not isinstance(n, numbers.Number):
            return False
    return True


def is_multi_point(x):
    """Verify a list or tuple is a valid GeoJSON MultiPoint."""
    if not isinstance(x, list) and not isinstance(x, tuple):
        return False
    for point in x:
        if not is_position(point):
            return False
    return True


def is_line_string(x):
    """Verify a list or tuple is a valid GeoJSON LineString."""
    if not isinstance(x, list) and not isinstance(x, tuple):
        return False
    if len(x) < 2:
        return False
    return is_multi_point(x)


def is_linear_ring(x):
    """Verify a list or tuple is a valid GeoJSON LinearRing."""
    if not isinstance(x, list) and not isinstance(x, tuple):
        return False
    if len(x) < 4:
        return False
    if not is_line_string(x):
        return False
    return equal_positions(x[0], x[len(x)-1])


def is_multi_line_string(x):
    """Verify a list or tuple is a valid GeoJSON MultiLineString."""
    if not isinstance(x, list) and not isinstance(x, tuple):
        return False
    for line_string in x:
        if not is_line_string(line_string):
            return False
    return True


def is_polygon(x):
    """Verify a list or tuple is a valid GeoJSON Polygon."""
    if not isinstance(x, list) and not isinstance(x, tuple):
        return False
    for linear_ring in x:
        if not is_linear_ring(linear_ring):
            return False
    # TODO Verify subsequent rings are contained within previous ones.
    return True


def is_multi_polygon(x):
    """Verify a list or tuple is a valid GeoJSON MultiPolygon."""
    if not isinstance(x, list) and not isinstance(x, tuple):
        return False
    for polygon in x:
        if not is_polygon(polygon):
            return False
    return True


def is_geometry(x):
    """Verify a dictionary is a valid GeoJSON Geometry object."""
    if not isinstance(x, dict):
        return False
    if 'type' in x.keys():
        if x['type'] == 'GeometryCollection':
            return is_geometry_collection(x)
        if x['type'] == 'Point':
            return is_position(x['coordinates'])
        if x['type'] == 'MultiPoint':
            return is_multi_point(x['coordinates'])
        if x['type'] == 'LineString':
            return is_line_string(x['coordinates'])
        if x['type'] == 'MultiLineString':
            return is_multi_line_string(x['coordinates'])
        if x['type'] == 'Polygon':
            return is_polygon(x['coordinates'])
        if x['type'] == 'MultiPolygon':
            return is_multi_polygon(x['coordinates'])
    return False


def is_geometry_collection(x):
    """Verify a dictionary is a valid GeoJSON GeometryCollection object."""
    if not isinstance(x, dict):
        return False
    if 'type' in x.keys() and x['type'] == 'GeometryCollection' and 'geometries' in x.keys():
        for geometry in x['geometries']:
            if not is_geometry(geometry):
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
            is_geometry(x['geometry']) and \
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


def is_geojson(x):
    """Verify a dictionary is a valid GeoJSON object."""
    if not isinstance(x, dict):
        return False
    return is_geometry(x) or is_feature(x) or is_feature_collection(x)
