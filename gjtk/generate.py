

import random


def Point(position):
    """ Create a valid GeoJSON Point geometry. """
    return {
       "type": "Point",
       "coordinates": position
    }


def GeometryCollection(geometries=None):
    """ Create a valid GeoJSON GeometryCollection. """
    return {
        "type": "GeometryCollection",
        "geometries": [] if geometries is None else geometries
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


def randomGeometryCollection(max_geometries=3):
    length = round(random.random()*100)%max_geometries
    return GeometryCollection(geometries=[randomGeometry() for i in range(int(length))])


def randomFeature():
    return Feature(geometry=randomGeometry(), properties=random.choice([None, {}, {'foo': 'bar'}]))
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

