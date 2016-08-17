"""Tests for README Example Data"""

from __future__ import absolute_import

import gjtk.validate


def test_is_point():
    """should return true when provided an example Point"""
    assert gjtk.validate.is_point({
        "type": "Point",
        "coordinates": [100.0, 0.0],
    })


def test_is_multi_point():
    """should return true when provided an example MultiPoint"""
    assert gjtk.validate.is_multi_point({
        "type": "MultiPoint",
        "coordinates": [[100.0, 0.0], [101.0, 1.0]],
    })


def test_is_line_string():
    """should return true when provided an example LineString"""
    assert gjtk.validate.is_line_string({
        "type": "LineString",
        "coordinates": [[100.0, 0.0], [101.0, 1.0]],
    })


def test_is_multi_line_string():
    """should return true when provided an example MultiLineString"""
    assert gjtk.validate.is_multi_line_string({
        "type": "MultiLineString",
        "coordinates": [
            [[100.0, 0.0], [101.0, 1.0]],
            [[102.0, 2.0], [103.0, 3.0]],
        ],
    })


def test_is_polygon():
    """should return true when provided an example Polygon"""
    assert gjtk.validate.is_polygon({
        "type": "Polygon",
        "coordinates": [
            [[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]],
        ],
    })


def test_is_polygon_with_hole():
    """should return true when provided an example Polygon"""
    assert gjtk.validate.is_polygon({
        "type": "Polygon",
        "coordinates": [
            [[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]],
            [[100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8], [100.2, 0.2]],
        ],
    })


def test_is_multi_polygon():
    """should return true when provided an example MultiPolygon"""
    assert gjtk.validate.is_multi_polygon({
        "type": "MultiPolygon",
        "coordinates": [
            [
                [[102.0, 2.0], [103.0, 2.0], [103.0, 3.0], [102.0, 3.0], [102.0, 2.0]],
            ],
            [
                [[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]],
                [[100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8], [100.2, 0.2]],
            ],
        ],
    })


def test_is_geometry_collection():
    """should return true when provided an example GeometryCollection"""
    assert gjtk.validate.is_geometry_collection({
        "type": "GeometryCollection",
        "geometries": [
            {
                "type": "Point",
                "coordinates": [100.0, 0.0],
            },
            {
                "type": "LineString",
                "coordinates": [[101.0, 0.0], [102.0, 1.0]],
            },
        ],
    })


def test_is_feature():
    """should return true when provided an example Feature"""
    assert gjtk.validate.is_feature({
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [125.6, 10.1],
        },
        "properties": {
            "name": "Dinagat Islands",
        },
    })


def test_is_feature_collection():
    """should return true when provided an example FeatureCollection"""
    assert gjtk.validate.is_feature_collection({
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [102.0, 0.5]},
                "properties": {"prop0": "value0"},
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "LineString",
                    "coordinates": [
                        [102.0, 0.0],
                        [103.0, 1.0],
                        [104.0, 0.0],
                        [105.0, 1.0],
                    ],
                },
                "properties": {
                    "prop0": "value0",
                    "prop1": 0.0,
                },
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [100.0, 0.0],
                            [101.0, 0.0],
                            [101.0, 1.0],
                            [100.0, 1.0],
                            [100.0, 0.0],
                        ],
                    ],
                },
                "properties": {
                    "prop0": "value0",
                    "prop1": {"this": "that"},
                },
            },
        ],
    })


def test_is_crs_1():
    """should return true when provided an example CRS"""
    assert gjtk.validate.is_crs({
        "type": "name",
        "properties": {
            "name": "urn:ogc:def:crs:OGC:1.3:CRS84",
        },
    })


def test_is_crs_2():
    """should return true when provided an example CRS"""
    assert gjtk.validate.is_crs({
        "type": "link",
        "properties": {
            "href": "http://example.com/crs/42",
            "type": "proj4",
        },
    })


def test_is_crs_3():
    """should return true when provided an example CRS"""
    assert gjtk.validate.is_crs({
        "type": "link",
        "properties": {
            "href": "data.crs",
            "type": "ogcwkt",
        },
    })


def test_is_link_1():
    """should return true when provided an example Link"""
    assert gjtk.validate.is_link({
        "href": "http://example.com/crs/42",
        "type": "proj4",
    })


def test_is_link_2():
    """should return true when provided an example Link"""
    assert gjtk.validate.is_link({
        "href": "data.crs",
        "type": "ogcwkt",
    })


def test_is_bbox_1():
    """should return true when provided an example Bbox"""
    assert gjtk.validate.is_bbox([-10.0, -10.0, 10.0, 10.0])


def test_is_bbox_2():
    """should return true when provided an example Bbox"""
    assert gjtk.validate.is_bbox([100.0, 0.0, 105.0, 1.0])
