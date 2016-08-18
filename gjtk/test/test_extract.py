"""Tests for gjtk.extract"""

from __future__ import absolute_import

import collections

import gjtk.example
import gjtk.extract
import gjtk.validate


# POSITIONS


def test_positions_of_point():
    """should return valid positions when provided a valid Point"""
    assert collections.Counter(map(
        str,
        gjtk.extract.positions_of(gjtk.example.POINT),
    )) == collections.Counter(map(
        str,
        [
            [100.0, 0.0],
        ],
    ))


def test_positions_of_multi_point():
    """should return valid positions when provided a valid MultiPoint"""
    assert collections.Counter(map(
        str,
        gjtk.extract.positions_of(gjtk.example.MULTI_POINT),
    )) == collections.Counter(map(
        str,
        [
            [100.0, 0.0],
            [101.0, 1.0],
        ],
    ))


def test_positions_of_line_string():
    """should return valid positions when provided a valid LineString"""
    assert collections.Counter(map(
        str,
        gjtk.extract.positions_of(gjtk.example.LINE_STRING),
    )) == collections.Counter(map(
        str,
        [
            [100.0, 0.0],
            [101.0, 1.0],
        ],
    ))


def test_positions_of_multi_line_string():
    """should return valid positions when provided a valid MultiLineString"""
    assert collections.Counter(map(
        str,
        gjtk.extract.positions_of(gjtk.example.MULTI_LINE_STRING),
    )) == collections.Counter(map(
        str,
        [
            [100.0, 0.0],
            [101.0, 1.0],
            [102.0, 2.0],
            [103.0, 3.0],
        ],
    ))


def test_positions_of_polygon_without_hole():
    """should return valid positions when provided a valid Polygon"""
    assert collections.Counter(map(
        str,
        gjtk.extract.positions_of(gjtk.example.POLYGON_WITHOUT_HOLE),
    )) == collections.Counter(map(
        str,
        [
            [100.0, 0.0],
            [101.0, 0.0],
            [101.0, 1.0],
            [100.0, 1.0],
            [100.0, 0.0],
        ],
    ))


def test_positions_of_polygon_with_hole():
    """should return valid positions when provided a valid Polygon"""
    assert collections.Counter(map(
        str,
        gjtk.extract.positions_of(gjtk.example.POLYGON_WITH_HOLE),
    )) == collections.Counter(map(
        str,
        [
            [100.0, 0.0],
            [101.0, 0.0],
            [101.0, 1.0],
            [100.0, 1.0],
            [100.0, 0.0],
            [100.2, 0.2],
            [100.8, 0.2],
            [100.8, 0.8],
            [100.2, 0.8],
            [100.2, 0.2],
        ],
    ))


def test_positions_of_multi_polygon():
    """should return valid positions when provided a valid MultiPolygon"""
    assert collections.Counter(map(
        str,
        gjtk.extract.positions_of(gjtk.example.MULTI_POLYGON),
    )) == collections.Counter(map(
        str,
        [
            [102.0, 2.0],
            [103.0, 2.0],
            [103.0, 3.0],
            [102.0, 3.0],
            [102.0, 2.0],
            [100.0, 0.0],
            [101.0, 0.0],
            [101.0, 1.0],
            [100.0, 1.0],
            [100.0, 0.0],
            [100.2, 0.2],
            [100.8, 0.2],
            [100.8, 0.8],
            [100.2, 0.8],
            [100.2, 0.2],
        ],
    ))


def test_positions_of_geometry_collection():
    """should return valid positions when provided a valid GeometryCollection"""
    assert collections.Counter(map(
        str,
        gjtk.extract.positions_of(gjtk.example.GEOMETRY_COLLECTION),
    )) == collections.Counter(map(
        str,
        [
            [100.0, 0.0],
            [101.0, 0.0],
            [102.0, 1.0],
        ],
    ))


def test_positions_of_feature():
    """should return valid positions when provided a valid Feature"""
    assert collections.Counter(map(
        str,
        gjtk.extract.positions_of(gjtk.example.FEATURE),
    )) == collections.Counter(map(
        str,
        [
            [125.6, 10.1],
        ],
    ))


def test_positions_of_feature_collection():
    """should return valid positions when provided a valid FeatureCollection"""
    assert collections.Counter(map(
        str,
        gjtk.extract.positions_of(gjtk.example.FEATURE_COLLECTION),
    )) == collections.Counter(map(
        str,
        [
            [102.0, 0.5],
            [102.0, 0.0],
            [103.0, 1.0],
            [104.0, 0.0],
            [105.0, 1.0],
            [100.0, 0.0],
            [101.0, 0.0],
            [101.0, 1.0],
            [100.0, 1.0],
            [100.0, 0.0],
        ],
    ))


def test_positions_of_geojson(geojson):
    """should return valid positions when provided any valid GeoJSON"""
    assert all(
        gjtk.validate.is_position(position) for position in gjtk.extract.positions_of(geojson),
    )


# GEOMETRIES


def test_geometries_of_point():
    """should return valid geometries when provided a valid Point"""
    assert gjtk.extract.geometries_of(gjtk.example.POINT) == \
        [gjtk.example.POINT]


def test_geometries_of_multi_point():
    """should return valid geometries when provided a valid MultiPoint"""
    assert gjtk.extract.geometries_of(gjtk.example.MULTI_POINT) == \
        [gjtk.example.MULTI_POINT]


def test_geometries_of_line_string():
    """should return valid geometries when provided a valid LineString"""
    assert gjtk.extract.geometries_of(gjtk.example.LINE_STRING) == \
        [gjtk.example.LINE_STRING]


def test_geometries_of_multi_line_string():
    """should return valid geometries when provided a valid MultiLineString"""
    assert gjtk.extract.geometries_of(gjtk.example.MULTI_LINE_STRING) == \
        [gjtk.example.MULTI_LINE_STRING]


def test_geometries_of_polygon_without_hole():
    """should return valid geometries when provided a valid Polygon"""
    assert gjtk.extract.geometries_of(gjtk.example.POLYGON_WITHOUT_HOLE) == \
        [gjtk.example.POLYGON_WITHOUT_HOLE]


def test_geometries_of_polygon_with_hole():
    """should return valid geometries when provided a valid Polygon"""
    assert gjtk.extract.geometries_of(gjtk.example.POLYGON_WITH_HOLE) == \
        [gjtk.example.POLYGON_WITH_HOLE]


def test_geometries_of_multi_polygon():
    """should return valid geometries when provided a valid MultiPolygon"""
    assert gjtk.extract.geometries_of(gjtk.example.MULTI_POLYGON) == \
        [gjtk.example.MULTI_POLYGON]


def test_geometries_of_geometry_collection():
    """should return valid geometries when provided a valid GeometryCollection"""
    assert gjtk.extract.geometries_of(gjtk.example.GEOMETRY_COLLECTION) == \
        gjtk.example.GEOMETRY_COLLECTION['geometries']


def test_geometries_of_feature():
    """should return valid geometries when provided a valid Feature"""
    assert gjtk.extract.geometries_of(gjtk.example.FEATURE) == \
        [gjtk.example.FEATURE['geometry']]


def test_geometries_of_feature_collection():
    """should return valid geometries when provided a valid FeatureCollection"""
    assert gjtk.extract.geometries_of(gjtk.example.FEATURE_COLLECTION) == \
        [feature['geometry'] for feature in gjtk.example.FEATURE_COLLECTION['features']]


def test_geometries_of_geojson(geojson):
    """should return valid geometries when provided any valid GeoJSON"""
    assert all(
        gjtk.validate.is_geometry(position) for position in gjtk.extract.geometries_of(geojson),
    )


# FEATURES


def test_features_of_feature(feature):
    """should return valid features when provided a valid Feature"""
    assert gjtk.extract.features_of(feature) == [feature]


def test_features_of_feature_collection(feature_collection):
    """should return valid features when provided a valid FeatureCollection"""
    assert gjtk.extract.features_of(feature_collection) == feature_collection['features']


def test_features_of_geojson(geojson):
    """should return valid features when provided any valid GeoJSON"""
    assert all(
        gjtk.validate.is_feature(position) for position in gjtk.extract.features_of(geojson),
    )
