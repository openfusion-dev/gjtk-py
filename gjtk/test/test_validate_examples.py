"""Tests for GeoJSON ToolKit Validation Utilities using Example Data"""

import random
import unittest

import gjtk


class ExampleTest(unittest.TestCase):

    """Tests for Validation using Example Data"""

    def test_is_point(self):
        """should return true when provided an example Point"""
        test_data = random.choice([
            {"type": "Point", "coordinates": [100.0, 0.0]},
        ])
        self.assertTrue(
            gjtk.validate.is_point(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_is_multi_point(self):
        """should return true when provided an example MultiPoint"""
        test_data = random.choice([
            {
                "type": "MultiPoint",
                "coordinates": [[100.0, 0.0], [101.0, 1.0]],
            },
        ])
        self.assertTrue(
            gjtk.validate.is_multi_point(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_is_line_string(self):
        """should return true when provided an example LineString"""
        test_data = random.choice([
            {
                "type": "LineString",
                "coordinates": [[100.0, 0.0], [101.0, 1.0]],
            },
        ])
        self.assertTrue(
            gjtk.validate.is_line_string(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_is_multi_line_string(self):
        """should return true when provided an example MultiLineString"""
        test_data = random.choice([
            {
                "type": "MultiLineString",
                "coordinates": [
                    [[100.0, 0.0], [101.0, 1.0]],
                    [[102.0, 2.0], [103.0, 3.0]],
                ],
            },
        ])
        self.assertTrue(
            gjtk.validate.is_multi_line_string(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_is_polygon(self):
        """should return true when provided an example Polygon"""
        test_data = random.choice([
            {
                "type": "Polygon",
                "coordinates": [
                    [[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]],
                ],
            },
            {
                "type": "Polygon",
                "coordinates": [
                    [[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]],
                    [[100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8], [100.2, 0.2]],
                ],
            },
        ])
        self.assertTrue(
            gjtk.validate.is_polygon(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_is_multi_polygon(self):
        """should return true when provided an example MultiPolygon"""
        test_data = random.choice([
            {
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
            },
        ])
        self.assertTrue(
            gjtk.validate.is_multi_polygon(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_is_geometry_collection(self):
        """should return true when provided an example GeometryCollection"""
        test_data = random.choice([
            {
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
            },
        ])
        self.assertTrue(
            gjtk.validate.is_geometry_collection(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_is_feature(self):
        """should return true when provided an example Feature"""
        test_data = random.choice([
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [125.6, 10.1],
                },
                "properties": {
                    "name": "Dinagat Islands",
                },
            },
        ])
        self.assertTrue(
            gjtk.validate.is_feature(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_is_feature_collection(self):
        """should return true when provided an example FeatureCollection"""
        test_data = random.choice([
            {
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
            }
        ])
        self.assertTrue(
            gjtk.validate.is_feature_collection(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_is_crs(self):
        """should return true when provided an example CRS"""
        test_data = random.choice([
            {
                "type": "name",
                "properties": {
                    "name": "urn:ogc:def:crs:OGC:1.3:CRS84",
                },
            },
            {
                "type": "link",
                "properties": {
                    "href": "http://example.com/crs/42",
                    "type": "proj4",
                },
            },
            {
                "type": "link",
                "properties": {
                    "href": "data.crs",
                    "type": "ogcwkt",
                },
            },
        ])
        self.assertTrue(
            gjtk.validate.is_crs(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_is_link(self):
        """should return true when provided an example Link"""
        test_data = random.choice([
            {
                "href": "http://example.com/crs/42",
                "type": "proj4",
            },
            {
                "href": "data.crs",
                "type": "ogcwkt",
            },
        ])
        self.assertTrue(
            gjtk.validate.is_link(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_is_bbox(self):
        """should return true when provided an example Bbox"""
        test_data = random.choice([
            [-10.0, -10.0, 10.0, 10.0],
            [100.0, 0.0, 105.0, 1.0],
        ])
        self.assertTrue(
            gjtk.validate.is_bbox(test_data),
            gjtk.test.error_message(test_data),
        )


if __name__ == "__main__":
    unittest.main()
