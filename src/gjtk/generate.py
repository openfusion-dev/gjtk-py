"""Generate GeoJSON objects from their components."""


def point(position):
    """Create a valid GeoJSON Point."""
    return {
        "type": "Point",
        "coordinates": position,
    }


def multi_point(coordinates=None):
    """Create a valid GeoJSON MultiPoint."""
    return {
        "type": "MultiPoint",
        "coordinates": [] if coordinates is None else coordinates,
    }


def line_string(coordinates):
    """Create a valid GeoJSON LineString."""
    return {
        "type": "LineString",
        "coordinates": coordinates,
    }


def multi_line_string(coordinates=None):
    """Create a valid GeoJSON MultiLineString."""
    return {
        "type": "MultiLineString",
        "coordinates": [] if coordinates is None else coordinates,
    }


def polygon(coordinates):
    """Create a valid GeoJSON Polygon."""
    return {
        "type": "Polygon",
        "coordinates": coordinates,
    }


def multi_polygon(coordinates=None):
    """Create a valid GeoJSON MultiPolygon."""
    return {
        "type": "MultiPolygon",
        "coordinates": [] if coordinates is None else coordinates,
    }


def geometry_collection(geometries=None):
    """Create a valid GeoJSON GeometryCollection."""
    return {
        "type": "GeometryCollection",
        "geometries": [] if geometries is None else geometries,
    }


def feature(geometry=None, properties=None):
    """Create a valid GeoJSON Feature."""
    return {
        "type": "Feature",
        "geometry": geometry,
        "properties": properties,
    }


def feature_collection(features=None):
    """Create a valid GeoJSON FeatureCollection."""
    return {
        "type": "FeatureCollection",
        "features": [] if features is None else features,
    }
