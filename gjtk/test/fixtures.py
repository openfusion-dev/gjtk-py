"""Pytest Fixtures"""

from __future__ import absolute_import

import copy
import json
import random

import pytest

import gjtk.example

# Pytest fixtures can rely on other fixtures.
# pylint: disable=redefined-outer-name


# Generic


@pytest.fixture
def immutable():
    """an immutable value"""
    return random.choice(((), None, True, 0, ''))


@pytest.fixture
def mutable():
    """a mutable value"""
    return random.choice(([], {}, object, lambda x: x))


@pytest.fixture
def types(immutable, mutable):
    """a value of any type"""
    return random.choice((immutable, mutable))


# GeoJSON


@pytest.fixture
def crs_without_properties(crs):
    """a GeoJSON CRS without a properties key"""
    del crs['properties']
    return crs


@pytest.fixture
def crs_without_type(crs):
    """a GeoJSON CRS without a type key"""
    del crs['type']
    return crs


@pytest.fixture
def feature_collection_with_bbox(feature_collection, bbox):
    """a GeoJSON FeatureCollection with a Bbox"""
    feature_collection['bbox'] = bbox
    return feature_collection


@pytest.fixture
def feature_collection_with_crs(feature_collection, crs):
    """a GeoJSON FeatureCollection with a CRS"""
    feature_collection['crs'] = crs
    return feature_collection


@pytest.fixture
def feature_collection_without_features(feature_collection):
    """a GeoJSON FeatureCollection without a features key"""
    del feature_collection['features']
    return feature_collection


@pytest.fixture
def feature_collection_without_type(feature_collection):
    """a GeoJSON FeatureCollection without a type key"""
    del feature_collection['type']
    return feature_collection


@pytest.fixture
def feature_with_bbox(feature, bbox):
    """a GeoJSON Feature with a Bbox"""
    feature['bbox'] = bbox
    return feature


@pytest.fixture
def feature_with_crs(feature, crs):
    """a GeoJSON Feature with a CRS"""
    feature['crs'] = crs
    return feature


@pytest.fixture
def feature_without_geometry(feature):
    """a GeoJSON Feature without a geometry key"""
    del feature['geometry']
    return feature


@pytest.fixture
def feature_without_type(feature):
    """a GeoJSON Feature without a type key"""
    del feature['type']
    return feature


@pytest.fixture
def geojson():
    """a valid GeoJSON object"""
    return random.choice([
        gjtk.random.geometry(),
        gjtk.random.feature(),
        gjtk.random.feature_collection(),
    ])


@pytest.fixture
def geojson_file(tmpdir, geojson):
    """a file that contains valid GeoJSON"""
    f = tmpdir.join('test.geojson')
    with f.open('w') as tmpfile:
        json.dump(geojson, tmpfile)
    return str(f)


@pytest.fixture
def geometry_with_bbox(geometry, bbox):
    """a GeoJSON Geometry with a Bbox"""
    geometry['bbox'] = bbox
    return geometry


@pytest.fixture
def geometry_with_crs(geometry, crs):
    """a GeoJSON Geometry with a CRS"""
    geometry['crs'] = crs
    return geometry


@pytest.fixture
def geometry_collection_without_geometries(geometry_collection):
    """a GeoJSON GeometryCollection without a geometries key"""
    del geometry_collection['geometries']
    return geometry_collection


@pytest.fixture
def geometry_collection_without_type(geometry_collection):
    """a GeoJSON GeometryCollection without a type key"""
    del geometry_collection['type']
    return geometry_collection


@pytest.fixture
def invalid_position(types):
    """an invalid GeoJSON Position"""
    return (types, [1], ['foo', 'bar'], [1, 'a'])


@pytest.fixture
def json_file(tmpdir):
    """a file that contains valid JSON that is not GeoJSON"""
    f = tmpdir.join('test.json')
    with f.open('w') as tmpfile:
        json.dump({'not': 'geojson'}, tmpfile)
    return str(f)


@pytest.fixture
def line_string_without_coordinates(line_string):
    """a GeoJSON LineString without a coordinates key"""
    del line_string['coordinates']
    return line_string


@pytest.fixture
def line_string_without_type(line_string):
    """a GeoJSON LineString without a type key"""
    del line_string['type']
    return line_string


@pytest.fixture
def link_without_href(link):
    """a GeoJSON Link without a href key"""
    del link['href']
    return link


@pytest.fixture
def link_without_type(link):
    """a GeoJSON Link without a type key"""
    link['type'] = None
    del link['type']
    return link


@pytest.fixture
def malformed_bbox(bbox):
    """an invalid GeoJSON Bbox with a valid structure"""
    return [max(bbox[0], bbox[1]), min(bbox[0], bbox[1])]


@pytest.fixture
def malformed_polygon():
    """an invalid GeoJSON Polygon with a valid structure"""
    polygon = copy.deepcopy(gjtk.example.POLYGON_WITH_HOLE)
    polygon['coordinates'] = [polygon['coordinates'][1], polygon['coordinates'][0]]
    return polygon


@pytest.fixture
def malformed_multi_polygon(multi_polygon):
    """an invalid GeoJSON MultiPolygon with a valid structure"""
    multi_polygon = copy.deepcopy(gjtk.example.MULTI_POLYGON)
    del multi_polygon['coordinates'][0][0][0]
    return multi_polygon


@pytest.fixture
def multi_line_string_without_coordinates(multi_line_string):
    """a GeoJSON MultiLineString without a coordinates key"""
    del multi_line_string['coordinates']
    return multi_line_string


@pytest.fixture
def multi_line_string_without_type(multi_line_string):
    """a GeoJSON MultiLineString without a type key"""
    del multi_line_string['type']
    return multi_line_string


@pytest.fixture
def multi_point_without_coordinates(multi_point):
    """a GeoJSON MultiPoint without a coordinates key"""
    del multi_point['coordinates']
    return multi_point


@pytest.fixture
def multi_point_without_type(multi_point):
    """a GeoJSON MultiPoint without a type key"""
    del multi_point['type']
    return multi_point


@pytest.fixture
def multi_polygon_without_coordinates(multi_polygon):
    """a GeoJSON MultiPolygon without a coordinates key"""
    del multi_polygon['coordinates']
    return multi_polygon


@pytest.fixture
def multi_polygon_without_type(multi_polygon):
    """a GeoJSON MultiPolygon without a type key"""
    del multi_polygon['type']
    return multi_polygon


@pytest.fixture
def point_without_coordinates(point):
    """a GeoJSON Point without a coordinates key"""
    del point['coordinates']
    return point


@pytest.fixture
def point_without_type(point):
    """a GeoJSON Point without a type key"""
    del point['type']
    return point


@pytest.fixture
def polygon_without_coordinates(polygon):
    """a GeoJSON Polygon without a coordinates key"""
    del polygon['coordinates']
    return polygon


@pytest.fixture
def polygon_without_type(polygon):
    """a GeoJSON Polygon without a type key"""
    del polygon['type']
    return polygon


@pytest.fixture
def text_file(tmpdir):
    """a file that does not contain valid JSON"""
    f = tmpdir.join('test.txt')
    with f.open('w'):
        f.write('not json')
    return str(f)


@pytest.fixture
def unequal_positions(position):
    """a 2-tuple pair of distinct GeoJSON Position"""
    position2 = list(position)
    position2[0] = position[0] + 1
    return position, position2
