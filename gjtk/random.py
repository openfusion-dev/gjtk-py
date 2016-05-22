"""Generate random GeoJSON elements."""

from __future__ import absolute_import

import random

import gjtk


def position(max_numbers=3, min_numbers=2):
    """Generate a random GeoJSON Position."""
    assert min_numbers > 1, "There must be at least two elements, and may be more."
    return [(random.random()-0.5)*100 for _ in range(random.randint(min_numbers, max_numbers))]


def point_coordinates():
    """Generate random coordinates for a GeoJSON Point."""
    return position()


def multi_point_coordinates(max_positions=6, min_positions=0):
    """Generate random coordinates for a GeoJSON MultiPoint."""
    return [position() for _ in range(random.randint(min_positions, max_positions))]


def line_string_coordinates(max_positions=6, min_positions=2):
    """Generate random coordinates for a GeoJSON LineString."""
    assert min_positions > 1, \
        'For type "LineString", the "coordinates" member must be an array of two or more positions.'
    return [position() for _ in range(random.randint(min_positions, max_positions))]


def linear_ring_coordinates():
    """Generate a random GeoJSON LinearRing."""
    origin = position()
    return [origin]+line_string_coordinates()+[origin]


def multi_line_string_coordinates(max_line_strings=6, min_line_strings=1):
    """Generate random coordinates for a GeoJSON MultiLineString."""
    return [
        line_string_coordinates()
        for _ in range(random.randint(min_line_strings, max_line_strings))
    ]


def polygon_coordinates():
    """Generate random coordinates for a GeoJSON Polygon."""
    quadrant = [
        1 if random.random() < 0.5 else -1,
        1 if random.random() < 0.5 else -1,
    ]
    center = [
        quadrant[0]*random.random()*1000,
        quadrant[1]*random.random()*1000
    ]
    apothem = (random.random()*100)+100
    delta = (random.random()*10)+1
    return [linear_ring_coordinates()] if random.random() < 0.5 else [
        [
            [center[0]-apothem, center[1]-apothem],  # left-bottom
            [center[0]-apothem, center[1]+apothem],  # left-top
            [center[0]+apothem, center[1]+apothem],  # right-top
            [center[0]+apothem, center[1]-apothem],  # right-bottom
            [center[0]-apothem, center[1]-apothem],  # left-bottom
        ],
        [
            [center[0]-apothem+delta, center[1]-apothem+delta],  # left-bottom
            [center[0]-apothem+delta, center[1]+apothem-delta],  # left-top
            [center[0]+apothem-delta, center[1]+apothem-delta],  # right-top
            [center[0]+apothem-delta, center[1]-apothem+delta],  # right-bottom
            [center[0]-apothem+delta, center[1]-apothem+delta],  # left-bottom
        ],
    ]


def multi_polygon_coordinates(max_polygons=6, min_polygons=1):
    """Generate random coordinates for a GeoJSON MultiPolygon."""
    return [polygon_coordinates() for _ in range(random.randint(min_polygons, max_polygons))]


def geometry():
    """Generate a random GeoJSON Geometry."""
    return random.choice([
        point,
        multi_point,
        line_string,
        multi_line_string,
        polygon,
        multi_polygon,
        geometry_collection,
    ])()


def point():
    """Generate a random GeoJSON Point."""
    return gjtk.generate.point(position=position())


def multi_point():
    """Generate a random GeoJSON MultiPoint."""
    return gjtk.generate.multi_point(coordinates=multi_point_coordinates())


def line_string():
    """Generate a random GeoJSON LineString."""
    return gjtk.generate.line_string(coordinates=line_string_coordinates())


def multi_line_string():
    """Generate a random GeoJSON MultiLineString."""
    return gjtk.generate.multi_line_string(coordinates=multi_line_string_coordinates())


def polygon():
    """Generate a random GeoJSON Polygon."""
    return gjtk.generate.polygon(coordinates=polygon_coordinates())


def multi_polygon():
    """Generate a random GeoJSON MultiPolygon."""
    return gjtk.generate.multi_polygon(coordinates=multi_polygon_coordinates())


def geometry_collection(max_geometries=3, min_geometries=0):
    """Generate a random GeoJSON GeometryCollection."""
    return gjtk.generate.geometry_collection(
        geometries=[geometry() for _ in range(random.randint(min_geometries, max_geometries))],
    )


def feature():
    """Generate a random GeoJSON Feature."""
    return gjtk.generate.feature(
        geometry=geometry(),
        properties=random.choice([
            None,
            {},
            {None: False},
        ]),
    )


def feature_collection(max_features=3, min_features=0):
    """Generate a random GeoJSON FeatureCollection."""
    return gjtk.generate.feature_collection(
        features=[feature() for _ in range(random.randint(min_features, max_features))],
    )


def crs():
    """Generate a random GeoJSON Coordinate Reference System."""
    return {
        "type": "link",
        "properties": link(),
    } if random.random() < 0.5 else {
        "type": "name",
        "properties": {
            "name": "urn:ogc:def:crs:OGC:1.3:CRS84" if random.random() < 0.5 else "EPSG:4326",
        },
    }


def link():
    """Generate a random GeoJSON Link."""
    new_link = {"href": "data.crs" if random.random() < 0.5 else "http://example.com/crs/42"}
    if random.random() < 0.5:
        new_link["type"] = random.choice(["proj4", "ogcwkt", "esriwkt"])
    return new_link


def bbox(max_dimensions=4, min_dimensions=2):
    """Generate a random GeoJSON Bounding Box."""
    lower_bounds = []
    upper_bounds = []
    for _ in range(random.randint(min_dimensions, max_dimensions)):
        lower_bounds.append(random.random() * -100)
        upper_bounds.append(random.random() * 100)
    return lower_bounds+upper_bounds
