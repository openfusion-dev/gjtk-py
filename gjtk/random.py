

from __future__ import absolute_import
import random

import gjtk


def Position(max_numbers=3, min_numbers=2):
    assert min_numbers > 1, "There must be at least two elements, and may be more."
    n = int((round(random.random()*100)%max_numbers)+min_numbers)
    return [(random.random()-0.5)*100 for i in range(n)]


def PointCoordinates():
    return Position()


def MultiPointCoordinates(max_positions=6, min_positions=0):
    n = int((round(random.random()*100)%max_positions)+min_positions)
    return [Position() for i in range(n)]


def LineStringCoordinates(max_positions=6, min_positions=2):
    assert min_positions > 1, 'For type "LineString", the "coordinates" member must be an array of two or more positions.'
    n = int((round(random.random()*100)%max_positions)+min_positions)
    return [Position() for i in range(n)]


def LinearRingCoordinates():
    origin = Position()
    return [origin]+LineStringCoordinates()+[origin]


def MultiLineStringCoordinates(max_line_strings=6, min_line_strings=1):
    n = int((round(random.random()*100)%max_line_strings)+min_line_strings)
    return [LineStringCoordinates() for i in range(n)]


def PolygonCoordinates():
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
    n = int((round(random.random()*100)%max_polygons)+min_polygons)
    return [PolygonCoordinates() for i in range(n)]


def Geometry():
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
    return gjtk.generate.Point(position=Position())


def MultiPoint():
    return gjtk.generate.MultiPoint(coordinates=MultiPointCoordinates())


def LineString():
    return gjtk.generate.LineString(coordinates=LineStringCoordinates())


def MultiLineString():
    return gjtk.generate.MultiLineString(coordinates=MultiLineStringCoordinates())


def Polygon():
    return gjtk.generate.Polygon(coordinates=PolygonCoordinates())


def MultiPolygon():
    return gjtk.generate.MultiPolygon(coordinates=MultiPolygonCoordinates())


def GeometryCollection(max_geometries=3, min_geometries=0):
    n = int((round(random.random()*100)%max_geometries)+min_geometries)
    return gjtk.generate.GeometryCollection(geometries=[Geometry() for i in range(n)])


def Feature():
    return gjtk.generate.Feature(
        geometry=Geometry(),
        properties=random.choice([
            None,
            {},
            {None: False}
        ])
    )


def FeatureCollection(max_features=3, min_features=0):
    n = int((round(random.random()*100)%max_features)+min_features)
    return gjtk.generate.FeatureCollection(features=[Feature() for i in range(n)])


def CRS():
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
    link = { "href": "data.crs" if random.random() < 0.5 else "http://example.com/crs/42" }
    if random.random() < 0.5:
        link["type"] = random.choice(["proj4", "ogcwkt", "esriwkt"])
    return link


def Bbox():  # TODO
    return [-180.0, -90.0, 180.0, 90.0]

