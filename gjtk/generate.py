

def Point(position):
    """ Create a valid GeoJSON Point geometry. """
    return {
       "type": "Point",
       "coordinates": position
    }


def MultiPoint(coordinates=None):
    """ Create a valid GeoJSON MultiPoint geometry. """
    return {
       "type": "MultiPoint",
       "coordinates": [] if coordinates is None else coordinates
    }


def LineString(coordinates):
    """ Create a valid GeoJSON LineString geometry. """
    return {
       "type": "LineString",
       "coordinates": coordinates
    }


def MultiLineString(coordinates=None):
    """ Create a valid GeoJSON MultiLineString geometry. """
    return {
       "type": "MultiLineString",
       "coordinates": [] if coordinates is None else coordinates
    }


def Polygon(coordinates):
    """ Create a valid GeoJSON Polygon geometry. """
    return {
       "type": "Polygon",
       "coordinates": coordinates
    }


def MultiPolygon(coordinates=None):
    """ Create a valid GeoJSON MultiPolygon geometry. """
    return {
       "type": "MultiPolygon",
       "coordinates": [] if coordinates is None else coordinates
    }


def GeometryCollection(geometries=None):
    """ Create a valid GeoJSON GeometryCollection. """
    return {
        "type": "GeometryCollection",
        "geometries": [] if geometries is None else geometries
    }


def Feature(geometry=None, properties=None):
    """ Create a valid GeoJSON Feature. """
    return {
        "type": "Feature",
        "geometry": geometry,
        "properties": properties
    }


def FeatureCollection(features=None):
    """ Create a valid GeoJSON FeatureCollection. """
    return {
        "type": "FeatureCollection",
        "features": [] if features is None else features
    }

