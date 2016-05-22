"""Validate GeoJSON objects."""

from __future__ import absolute_import

from numbers import Number
from matplotlib.path import Path


def boolean_fail(f):
    """Decorate a validation function."""
    def wrapped_f(*args, **kwargs):
        """Return False if an exception is raised."""
        try:
            return f(*args, **kwargs)
        except:  # pylint: disable=bare-except
            return False
    return wrapped_f


@boolean_fail
def is_geojson(anything):
    """ Validate a GeoJSON object. """
    return (
        is_geometry(anything) or
        is_feature(anything) or
        is_feature_collection(anything)
    )


@boolean_fail
def is_geometry(anything):
    """ Validate a GeoJSON Geometry. """
    return (
        is_point(anything) or
        is_multi_point(anything) or
        is_line_string(anything) or
        is_multi_line_string(anything) or
        is_polygon(anything) or
        is_multi_polygon(anything) or
        is_geometry_collection(anything)
    )


@boolean_fail
def is_position(anything):
    """ Validate a GeoJSON Position. """
    return (
        isinstance(anything, list) and
        len(anything) > 1 and
        all(isinstance(n, Number) for n in anything)
    )


@boolean_fail
def is_point_coordinates(anything):
    """ Validate the coordinates of a GeoJSON Point. """
    return is_position(anything)


@boolean_fail
def is_multi_point_coordinates(anything):
    """ Validate the coordinates of a GeoJSON MultiPoint. """
    return (
        isinstance(anything, list) and
        all(is_position(position) for position in anything)
    )


@boolean_fail
def is_line_string_coordinates(anything):
    """ Validate the coordinates of a GeoJSON LineString. """
    return (
        isinstance(anything, list) and
        len(anything) > 1 and
        all(is_position(position) for position in anything)
    )


@boolean_fail
def is_linear_ring_coordinates(anything):
    """ Validate a GeoJSON LinearRing. """
    return (
        isinstance(anything, list) and
        len(anything) > 3 and
        is_line_string_coordinates(anything) and
        equal_positions(anything[0], anything[len(anything)-1])
    )


@boolean_fail
def is_multi_line_string_coordinates(anything):  # pylint: disable=invalid-name
    """ Validate the coordinates of a GeoJSON MultiLineString. """
    return (
        isinstance(anything, list) and
        all(is_line_string_coordinates(line_string_coords) for line_string_coords in anything)
    )


@boolean_fail
def is_polygon_coordinates(anything):
    """ Validate the coordinates of a GeoJSON Polygon. """
    if not isinstance(anything, list):
        return False
    prev = None
    for linear_ring in anything:
        if not is_linear_ring_coordinates(linear_ring):
            return False
        if prev is not None and not contained_polygon(linear_ring, prev):
            return False
        prev = linear_ring
    return True


@boolean_fail
def is_multi_polygon_coordinates(anything):
    """ Validate the coordinates of a GeoJSON MultiPolygon. """
    return (
        isinstance(anything, list) and
        all(is_polygon_coordinates(polygon_coords) for polygon_coords in anything)
    )


@boolean_fail
def is_point(anything):
    """ Validate a GeoJSON Point. """
    return (
        isinstance(anything, dict) and
        anything.get("type") == "Point" and
        is_point_coordinates(anything.get("coordinates")) and
        has_crs(anything) and
        has_bbox(anything)
    )


@boolean_fail
def is_multi_point(anything):
    """ Validate a GeoJSON MultiPoint. """
    return (
        isinstance(anything, dict) and
        anything.get("type") == "MultiPoint" and
        is_multi_point_coordinates(anything.get("coordinates")) and
        has_crs(anything) and
        has_bbox(anything)
    )


@boolean_fail
def is_line_string(anything):
    """ Validate a GeoJSON LineString. """
    return (
        isinstance(anything, dict) and
        anything.get("type") == "LineString" and
        is_line_string_coordinates(anything.get("coordinates")) and
        has_crs(anything) and
        has_bbox(anything)
    )


@boolean_fail
def is_multi_line_string(anything):
    """ Validate a GeoJSON MultiLineString. """
    return (
        isinstance(anything, dict) and
        anything.get("type") == "MultiLineString" and
        is_multi_line_string_coordinates(anything.get("coordinates")) and
        has_crs(anything) and
        has_bbox(anything)
    )


@boolean_fail
def is_polygon(anything):
    """ Validate a GeoJSON Polygon. """
    return (
        isinstance(anything, dict) and
        anything.get("type") == "Polygon" and
        is_polygon_coordinates(anything.get("coordinates")) and
        has_crs(anything) and
        has_bbox(anything)
    )


@boolean_fail
def is_multi_polygon(anything):
    """ Validate a GeoJSON MultiPolygon. """
    return (
        isinstance(anything, dict) and
        anything.get("type") == "MultiPolygon" and
        is_multi_polygon_coordinates(anything.get("coordinates")) and
        has_crs(anything) and
        has_bbox(anything)
    )


@boolean_fail
def is_geometry_collection(anything):
    """ Validate a GeoJSON GeometryCollection. """
    return (
        isinstance(anything, dict) and
        anything.get("type") == "GeometryCollection" and
        ("geometries" in anything) and
        all(is_geometry(geometry) for geometry in anything["geometries"]) and
        has_crs(anything) and
        has_bbox(anything)
    )


@boolean_fail
def is_feature(anything):
    """ Validate a GeoJSON Feature. """
    return (
        isinstance(anything, dict) and
        anything.get("type") == "Feature" and
        ("geometry" in anything) and
        (
            anything["geometry"] is None or
            is_geometry(anything["geometry"])
        ) and
        has_crs(anything) and
        has_bbox(anything)
    )


@boolean_fail
def is_feature_collection(anything):
    """ Validate a GeoJSON FeatureCollection. """
    return (
        isinstance(anything, dict) and
        anything.get("type") == "FeatureCollection" and
        ("features" in anything) and
        all(is_feature(feature) for feature in anything.get("features")) and
        has_crs(anything) and
        has_bbox(anything)
    )


@boolean_fail
def is_crs(anything):
    """ Validate a GeoJSON Coordinate Reference System. """
    return (
        isinstance(anything, dict) and
        (
            (
                anything.get("type") == "name" and
                anything.get("properties") is not None and
                len(str(anything["properties"].get("name", ""))) > 0
            ) or
            (
                anything.get("type") == "link" and
                is_link(anything.get("properties"))
            )
        )
    )


@boolean_fail
def has_crs(anything, required=False):
    """ Validate the crs property of a GeoJSON object. """
    return (
        isinstance(anything, dict) and
        is_crs(anything.get("crs"))
    ) if required else (
        isinstance(anything, dict) and
        (
            anything.get("crs") is None or
            is_crs(anything["crs"])
        )
    )


@boolean_fail
def is_link(anything):
    """ Validate a GeoJSON Link. """
    return (
        isinstance(anything, dict) and
        (
            anything.get("type") is None or
            len(str(anything["type"])) > 0
        ) and
        str(anything["href"])
    )


@boolean_fail
def is_bbox(anything):
    """ Validate a GeoJSON Bounding Box. """
    if not isinstance(anything, list) or len(anything) < 1 or len(anything) % 2 != 0:
        return False
    pivot = int(len(anything) / 2)
    for i in range(pivot):
        if anything[i] > anything[i+pivot]:
            return False
    return True


@boolean_fail
def has_bbox(anything, required=False):
    """ Validate the bbox property of a GeoJSON object. """
    return (
        isinstance(anything, dict) and
        is_bbox(anything.get("bbox"))
    ) if required else (
        isinstance(anything, dict) and
        (
            anything.get("bbox") is None or
            is_bbox(anything["bbox"])
        )
    )


# COMPARISON


@boolean_fail
def equal_positions(this, that):
    """ Compare two GeoJSON Positions for equality. """
    return (
        is_position(this) and is_position(that) and
        len(this) == len(that) and
        all(this[i] == that[i] for i in range(len(this)))
    )


@boolean_fail
def contained_polygon(inner, outer):
    """ Determine whether one GeoJSON LinearRing contains another. """
    outer_path = Path(outer)
    return all(outer_path.contains_point([position[0], position[1]]) for position in inner)
