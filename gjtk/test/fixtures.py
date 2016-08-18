"""Pytest Fixtures"""

from __future__ import absolute_import

import copy

import pytest

import gjtk.example

# pylint: disable=unused-wildcard-import
from gjtk.random import *  # pylint: disable=wildcard-import
# pylint: disable=redefined-outer-name, missing-docstring


# Generic


@pytest.fixture
def immutable():
    return (), None, True, 0, ''


@pytest.fixture
def mutable():
    return ([], {}, object, lambda x: x)


@pytest.fixture
def types(immutable, mutable):
    return immutable + mutable


# GeoJSON


@pytest.fixture
def crs_without_properties(crs):
    del crs['properties']
    return crs


@pytest.fixture
def crs_without_type(crs):
    del crs['type']
    return crs


@pytest.fixture
def feature_collection_with_bbox(feature_collection, bbox):
    feature_collection['bbox'] = bbox
    return feature_collection


@pytest.fixture
def feature_collection_with_crs(feature_collection, crs):
    feature_collection['crs'] = crs
    return feature_collection


@pytest.fixture
def feature_collection_without_features(feature_collection):
    del feature_collection['features']
    return feature_collection


@pytest.fixture
def feature_collection_without_type(feature_collection):
    del feature_collection['type']
    return feature_collection


@pytest.fixture
def feature_with_bbox(feature, bbox):
    feature['bbox'] = bbox
    return feature


@pytest.fixture
def feature_with_crs(feature, crs):
    feature['crs'] = crs
    return feature


@pytest.fixture
def feature_without_geometry(feature):
    del feature['geometry']
    return feature


@pytest.fixture
def feature_without_type(feature):
    del feature['type']
    return feature


@pytest.fixture
def geometry_with_bbox(geometry, bbox):
    geometry['bbox'] = bbox
    return geometry


@pytest.fixture
def geojson():
    return random.choice([
        gjtk.random.geometry(),
        gjtk.random.feature(),
        gjtk.random.feature_collection(),
    ])


@pytest.fixture
def geometry_with_crs(geometry, crs):
    geometry['crs'] = crs
    return geometry


@pytest.fixture
def geometry_collection_without_geometries(geometry_collection):
    del geometry_collection['geometries']
    return geometry_collection


@pytest.fixture
def geometry_collection_without_type(geometry_collection):
    del geometry_collection['type']
    return geometry_collection


@pytest.fixture
def invalid_position(types):
    return types + ([1], ['foo', 'bar'], [1, 'a'])


@pytest.fixture
def line_string_without_coordinates(line_string):
    del line_string['coordinates']
    return line_string


@pytest.fixture
def line_string_without_type(line_string):
    del line_string['type']
    return line_string


@pytest.fixture
def link_without_href(link):
    del link['href']
    return link


@pytest.fixture
def link_without_type(link):
    link['type'] = None
    del link['type']
    return link


@pytest.fixture
def malformed_bbox(bbox):
    return [max(bbox[0], bbox[1]), min(bbox[0], bbox[1])]


@pytest.fixture
def malformed_polygon():
    polygon = copy.deepcopy(gjtk.example.POLYGON_WITH_HOLE)
    polygon['coordinates'] = [polygon['coordinates'][1], polygon['coordinates'][0]]
    return polygon


@pytest.fixture
def malformed_multi_polygon(multi_polygon):
    multi_polygon = copy.deepcopy(gjtk.example.MULTI_POLYGON)
    del multi_polygon['coordinates'][0][0][0]
    return multi_polygon


@pytest.fixture
def multi_line_string_without_coordinates(multi_line_string):
    del multi_line_string['coordinates']
    return multi_line_string


@pytest.fixture
def multi_line_string_without_type(multi_line_string):
    del multi_line_string['type']
    return multi_line_string


@pytest.fixture
def multi_point_without_coordinates(multi_point):
    del multi_point['coordinates']
    return multi_point


@pytest.fixture
def multi_point_without_type(multi_point):
    del multi_point['type']
    return multi_point


@pytest.fixture
def multi_polygon_without_coordinates(multi_polygon):
    del multi_polygon['coordinates']
    return multi_polygon


@pytest.fixture
def multi_polygon_without_type(multi_polygon):
    del multi_polygon['type']
    return multi_polygon


@pytest.fixture
def point_without_coordinates(point):
    del point['coordinates']
    return point


@pytest.fixture
def point_without_type(point):
    del point['type']
    return point


@pytest.fixture
def polygon_without_coordinates(polygon):
    del polygon['coordinates']
    return polygon


@pytest.fixture
def polygon_without_type(polygon):
    del polygon['type']
    return polygon


@pytest.fixture
def unequal_positions(position):
    position2 = list(position)
    position2[0] = position[0] + 1
    return position, position2
