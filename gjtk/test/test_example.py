"""Tests for gjtk.example"""

from __future__ import absolute_import

import gjtk.example
import gjtk.validate


def test_is_point():
    """should return true when provided an example Point"""
    assert gjtk.validate.is_point(gjtk.example.POINT)


def test_is_multi_point():
    """should return true when provided an example MultiPoint"""
    assert gjtk.validate.is_multi_point(gjtk.example.MULTI_POINT)


def test_is_line_string():
    """should return true when provided an example LineString"""
    assert gjtk.validate.is_line_string(gjtk.example.LINE_STRING)


def test_is_multi_line_string():
    """should return true when provided an example MultiLineString"""
    assert gjtk.validate.is_multi_line_string(gjtk.example.MULTI_LINE_STRING)


def test_is_polygon_without_hole():
    """should return true when provided an example Polygon"""
    assert gjtk.validate.is_polygon(gjtk.example.POLYGON_WITHOUT_HOLE)


def test_is_polygon_with_hole():
    """should return true when provided an example Polygon"""
    assert gjtk.validate.is_polygon(gjtk.example.POLYGON_WITH_HOLE)


def test_is_multi_polygon():
    """should return true when provided an example MultiPolygon"""
    assert gjtk.validate.is_multi_polygon(gjtk.example.MULTI_POLYGON)


def test_is_geometry_collection():
    """should return true when provided an example GeometryCollection"""
    assert gjtk.validate.is_geometry_collection(gjtk.example.GEOMETRY_COLLECTION)


def test_is_feature():
    """should return true when provided an example Feature"""
    assert gjtk.validate.is_feature(gjtk.example.FEATURE)


def test_is_feature_collection():
    """should return true when provided an example FeatureCollection"""
    assert gjtk.validate.is_feature_collection(gjtk.example.FEATURE_COLLECTION)


def test_is_crs_1():
    """should return true when provided an example CRS"""
    assert gjtk.validate.is_crs(gjtk.example.CRS_1)


def test_is_crs_2():
    """should return true when provided an example CRS"""
    assert gjtk.validate.is_crs(gjtk.example.CRS_2)


def test_is_crs_3():
    """should return true when provided an example CRS"""
    assert gjtk.validate.is_crs(gjtk.example.CRS_3)


def test_is_link_1():
    """should return true when provided an example Link"""
    assert gjtk.validate.is_link(gjtk.example.LINK_1)


def test_is_link_2():
    """should return true when provided an example Link"""
    assert gjtk.validate.is_link(gjtk.example.LINK_2)


def test_is_bbox_1():
    """should return true when provided an example Bbox"""
    assert gjtk.validate.is_bbox(gjtk.example.BBOX_1)


def test_is_bbox_2():
    """should return true when provided an example Bbox"""
    assert gjtk.validate.is_bbox(gjtk.example.BBOX_2)
