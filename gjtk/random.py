

from __future__ import absolute_import
import random

import gjtk


def Position(max_numbers=3, min_numbers=2):
    """ Generate a random GeoJSON Position. """
    assert min_numbers > 1, "There must be at least two elements, and may be more."
    return [(random.random()-0.5)*100 for i in range(random.randint(min_numbers, max_numbers))]


def PointCoordinates():
    """ Generate random coordinates for a GeoJSON Point. """
    return Position()


def MultiPointCoordinates(max_positions=6, min_positions=0):
    """ Generate random coordinates for a GeoJSON MultiPoint. """
    return [Position() for i in range(random.randint(min_positions, max_positions))]


def LineStringCoordinates(max_positions=6, min_positions=2):
    """ Generate random coordinates for a GeoJSON LineString. """
    assert min_positions > 1, 'For type "LineString", the "coordinates" member must be an array of two or more positions.'
    return [Position() for i in range(random.randint(min_positions, max_positions))]


def LinearRingCoordinates():
    """ Generate a random GeoJSON LinearRing. """
    origin = Position()
    return [origin]+LineStringCoordinates()+[origin]


def MultiLineStringCoordinates(max_line_strings=6, min_line_strings=1):
    """ Generate random coordinates for a GeoJSON MultiLineString. """
    return [LineStringCoordinates() for i in range(random.randint(min_line_strings, max_line_strings))]


def PolygonCoordinates():
    """ Generate random coordinates for a GeoJSON Polygon. """
    quadrant = [
        1 if random.random() < 0.5 else -1,
        1 if random.random() < 0.5 else -1
    ]
    center = [
        quadrant[0]*random.random()*1000,
        quadrant[1]*random.random()*1000
    ]
    apothem = (random.random()*100)+100
    delta = (random.random()*10)+1
    return [LinearRingCoordinates()] if random.random() < 0.5 else [
        [
            [center[0]-apothem, center[1]-apothem],  #  left-bottom
            [center[0]-apothem, center[1]+apothem],  #  left-top
            [center[0]+apothem, center[1]+apothem],  # right-top
            [center[0]+apothem, center[1]-apothem],  # right-bottom
            [center[0]-apothem, center[1]-apothem]   #  left-bottom
        ],
        [
            [center[0]-apothem+delta, center[1]-apothem+delta],  #  left-bottom
            [center[0]-apothem+delta, center[1]+apothem-delta],  #  left-top
            [center[0]+apothem-delta, center[1]+apothem-delta],  # right-top
            [center[0]+apothem-delta, center[1]-apothem+delta],  # right-bottom
            [center[0]-apothem+delta, center[1]-apothem+delta]   #  left-bottom
        ]
    ]


def MultiPolygonCoordinates(max_polygons=6, min_polygons=1):
    """ Generate random coordinates for a GeoJSON MultiPolygon. """
    return [PolygonCoordinates() for i in range(random.randint(min_polygons, max_polygons))]


def Geometry():
    """ Generate a random GeoJSON Geometry. """
    return random.choice([
      Point,
      MultiPoint,
      LineString,
      MultiLineString,
      Polygon,
      MultiPolygon,
      GeometryCollection
    ])()


def Point():
    """ Generate a random GeoJSON Point. """
    return gjtk.generate.Point(position=Position())


def MultiPoint():
    """ Generate a random GeoJSON MultiPoint. """
    return gjtk.generate.MultiPoint(coordinates=MultiPointCoordinates())


def LineString():
    """ Generate a random GeoJSON LineString. """
    return gjtk.generate.LineString(coordinates=LineStringCoordinates())


def MultiLineString():
    """ Generate a random GeoJSON MultiLineString. """
    return gjtk.generate.MultiLineString(coordinates=MultiLineStringCoordinates())


def Polygon():
    """ Generate a random GeoJSON Polygon. """
    return gjtk.generate.Polygon(coordinates=PolygonCoordinates())


def MultiPolygon():
    """ Generate a random GeoJSON MultiPolygon. """
    return gjtk.generate.MultiPolygon(coordinates=MultiPolygonCoordinates())


def GeometryCollection(max_geometries=3, min_geometries=0):
    """ Generate a random GeoJSON GeometryCollection. """
    return gjtk.generate.GeometryCollection(
        geometries=[Geometry() for i in range(random.randint(min_geometries, max_geometries))]
    )


def Feature():
    """ Generate a random GeoJSON Feature. """
    return gjtk.generate.Feature(
        geometry=Geometry(),
        properties=random.choice([
            None,
            {},
            {None: False}
        ])
    )


def FeatureCollection(max_features=3, min_features=0):
    """ Generate a random GeoJSON FeatureCollection. """
    return gjtk.generate.FeatureCollection(
        features=[Feature() for i in range(random.randint(min_features, max_features))]
    )


def CRS():
    """ Generate a random GeoJSON Coordinate Reference System. """
    return {
        "type": "link",
        "properties": Link()
    } if random.random() < 0.5 else {
        "type": "name",
        "properties": {
            "name": "urn:ogc:def:crs:OGC:1.3:CRS84" if random.random() < 0.5 else "EPSG:4326"
        }
    }


def Link():
    """ Generate a random GeoJSON Link. """
    link = { "href": "data.crs" if random.random() < 0.5 else "http://example.com/crs/42" }
    if random.random() < 0.5:
        link["type"] = random.choice(["proj4", "ogcwkt", "esriwkt"])
    return link


def Bbox(max_dimensions=4, min_dimensions=2):
    """ Generate a random GeoJSON Bounding Box. """
    lower_bounds = []
    upper_bounds = []
    for i in range(random.randint(min_dimensions, max_dimensions)):
        lower_bounds.append(random.random()*-100)
        upper_bounds.append(random.random()* 100)
    return lower_bounds+upper_bounds

