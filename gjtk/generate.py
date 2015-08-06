

import random


def Point(position):
    """ Create a valid GeoJSON Point geometry. """
    return {
       "type": "Point",
       "coordinates": position
    }


def Feature(geometry, properties=None):
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


def GeometryCollection(geometries=None):
    """ Create a valid GeoJSON GeometryCollection. """
    return {
        "type": "GeometryCollection",
        "geometries": [] if geometries is None else geometries
    }


def randomPosition():
    length = (round(random.random()*100)%6)+2
    return [(random.random()-0.5)*100 for i in range(int(length))]


def randomPointCoordinates():
    return randomPosition()


def randomMultiPointCoordinates():
    length = (round(random.random()*100)%6)+1
    return [randomPosition() for i in range(int(length))]


def randomLineStringCoordinates():
    length = (round(random.random()*100)%6)+2
    return [randomPosition() for i in range(int(length))]


def randomLinearRingCoordinates():
    origin = randomPosition()
    return [origin]+randomLineStringCoordinates()+[origin]


def randomMultiLineStringCoordinates():
    length = (round(random.random()*100)%6)+1
    return [randomLineStringCoordinates() for i in range(int(length))]


def randomPolygonCoordinates():  # TODO
    return [randomLinearRingCoordinates()] if random.random() < 0.5 else [
      [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0] ],
      [ [100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8], [100.2, 0.2] ]
    ]


def randomMultiPolygonCoordinates():
    length = (round(random.random()*100)%6)+1
    return [randomPolygonCoordinates() for i in range(int(length))]


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
    return {
        "type": "Point",
        "coordinates": randomPointCoordinates()
    }


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


def randomGeometryCollection():
    length = round(random.random()*100)%3
    return {
      "type": "GeometryCollection",
      "geometries": [randomGeometry() for i in range(int(length))]
    }


def randomFeature():
    return {
      "type": "Feature",
      "geometry": randomGeometry(),
      "properties": random.choice([None, {}, {'foo': 'bar'}])
    }


def randomFeatureCollection():
    length = round(random.random()*100)%3
    return {
      "type": "FeatureCollection",
      "features": [randomFeature() for i in range(int(length))]
    }


def randomCRS():  # TODO
    return {
        "type": "link",
        "properties": randomLink()
    } if random.random() < 0.5 else {
        "type": "name",
        "properties": {
            "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
        }
    }


def randomLink():  # TODO
    return {
      "href": "data.crs",
      "type": "ogcwkt"
    }


def randomBbox():  # TODO
    return [-180.0, -90.0, 180.0, 90.0]

