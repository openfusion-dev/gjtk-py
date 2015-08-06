

import random


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


def randomPosition(max_numbers=3, min_numbers=2):
    assert min_numbers > 1, "There must be at least two elements, and may be more."
    n = int((round(random.random()*100)%max_numbers)+min_numbers)
    return [(random.random()-0.5)*100 for i in range(n)]


def randomPointCoordinates():
    return randomPosition()


def randomMultiPointCoordinates(max_positions=6, min_positions=0):
    n = int((round(random.random()*100)%max_positions)+min_positions)
    return [randomPosition() for i in range(n)]


def randomLineStringCoordinates(max_positions=6, min_positions=2):
    assert min_positions > 1, 'For type "LineString", the "coordinates" member must be an array of two or more positions.'
    n = int((round(random.random()*100)%max_positions)+min_positions)
    return [randomPosition() for i in range(n)]


def randomLinearRingCoordinates():
    origin = randomPosition()
    return [origin]+randomLineStringCoordinates()+[origin]


def randomMultiLineStringCoordinates(max_line_strings=6, min_line_strings=1):
    n = int((round(random.random()*100)%max_line_strings)+min_line_strings)
    return [randomLineStringCoordinates() for i in range(n)]


def randomPolygonCoordinates():
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
    return [randomLinearRingCoordinates()] if random.random() < 0.5 else [
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


def randomMultiPolygonCoordinates(max_polygons=6, min_polygons=1):
    n = int((round(random.random()*100)%max_polygons)+min_polygons)
    return [randomPolygonCoordinates() for i in range(n)]


def randomGeometry():
    return random.choice([
      randomPoint,
      randomMultiPoint,
      randomLineString,
      randomMultiLineString,
      randomPolygon,
      randomMultiPolygon,
      randomGeometryCollection
    ])()


def randomPoint():
    return Point(position=randomPosition())


def randomMultiPoint():
    return {
      "type": "MultiPoint",
      "coordinates": randomMultiPointCoordinates()
    }


def randomLineString():
    return {
      "type": "LineString",
      "coordinates": randomLineStringCoordinates()
    }


def randomMultiLineString():
    return {
      "type": "MultiLineString",
      "coordinates": randomMultiLineStringCoordinates()
    }


def randomPolygon():
    return {
      "type": "Polygon",
      "coordinates": randomPolygonCoordinates()
    }


def randomMultiPolygon():
    return {
      "type": "MultiPolygon",
      "coordinates": randomMultiPolygonCoordinates()
    }


def randomGeometryCollection(max_geometries=3, min_geometries=0):
    n = int((round(random.random()*100)%max_geometries)+min_geometries)
    return GeometryCollection(geometries=[randomGeometry() for i in range(n)])


def randomFeature():
    return Feature(
        geometry=randomGeometry(),
        properties=random.choice([
            None,
            {},
            {None: False}
        ])
    )


def randomFeatureCollection(max_features=3, min_features=0):
    n = int((round(random.random()*100)%max_features)+min_features)
    return FeatureCollection(features=[randomFeature() for i in range(n)])


def randomCRS():
    return {
        "type": "link",
        "properties": randomLink()
    } if random.random() < 0.5 else {
        "type": "name",
        "properties": {
            "name": "urn:ogc:def:crs:OGC:1.3:CRS84" if random.random() < 0.5 else "EPSG:4326"
        }
    }


def randomLink():
    link = { "href": "data.crs" if random.random() < 0.5 else "http://example.com/crs/42" }
    if random.random() < 0.5:
        link["type"] = random.choice(["proj4", "ogcwkt", "esriwkt"])
    return link


def randomBbox():  # TODO
    return [-180.0, -90.0, 180.0, 90.0]

