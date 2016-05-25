"""Tests for GeoJSON ToolKit Generation Utilities"""

import random
import unittest

import gjtk


class PointTest(unittest.TestCase):

    """Tests for Position Generation"""

    def test_valid_position(self):
        """should return a valid Point object when provided a valid Position"""
        test_data = gjtk.random.position(max_numbers=6)
        test_result = gjtk.generate.point(test_data)
        self.assertTrue(
            gjtk.validate.is_point(test_result),
            gjtk.test.error_message(test_data, test_result),
        )


class MultiPointTest(unittest.TestCase):

    """Tests for MultiPoint Generation"""

    def test_valid_coordinates(self):
        """should return a valid MultiPoint object when provided valid coordinates"""
        test_data = gjtk.random.multi_point_coordinates()
        test_result = gjtk.generate.multi_point(coordinates=test_data)
        self.assertTrue(
            gjtk.validate.is_multi_point(test_result),
            gjtk.test.error_message(test_data, test_result),
        )


class LineStringTest(unittest.TestCase):

    """Tests for LineString Generation"""

    def test_valid_coordinates(self):
        """should return a valid LineString object when provided valid coordinates"""
        test_data = gjtk.random.line_string_coordinates()
        test_result = gjtk.generate.line_string(coordinates=test_data)
        self.assertTrue(
            gjtk.validate.is_line_string(test_result),
            gjtk.test.error_message(test_data, test_result),
        )


class MultiLineStringTest(unittest.TestCase):

    """Tests for MultiLineString Generation"""

    def test_valid_coordinates(self):
        """should return a valid MultiLineString object when provided valid coordinates"""
        test_data = gjtk.random.multi_line_string_coordinates()
        test_result = gjtk.generate.multi_line_string(coordinates=test_data)
        self.assertTrue(
            gjtk.validate.is_multi_line_string(test_result),
            gjtk.test.error_message(test_data, test_result),
        )


class PolygonTest(unittest.TestCase):

    """Tests for Polygon Generation"""

    def test_valid_coordinates(self):
        """should return a valid Polygon object when provided valid coordinates"""
        test_data = gjtk.random.polygon_coordinates()
        test_result = gjtk.generate.polygon(coordinates=test_data)
        self.assertTrue(
            gjtk.validate.is_polygon(test_result),
            gjtk.test.error_message(test_data, test_result),
        )


class MultiPolygonTest(unittest.TestCase):

    """Tests for MultiPolygon Generation"""

    def test_valid_coordinates(self):
        """should return a valid MultiPolygon object when provided valid coordinates"""
        test_data = gjtk.random.multi_polygon_coordinates()
        test_result = gjtk.generate.multi_polygon(coordinates=test_data)
        self.assertTrue(
            gjtk.validate.is_multi_polygon(test_result),
            gjtk.test.error_message(test_data, test_result),
        )


class GeometryCollectionTest(unittest.TestCase):

    """Tests for GeometryCollection Generation"""

    def test_valid_geometries(self):
        """should return a valid GeometryCollection object when provided valid Geometries"""
        length = round(random.random() * 100) % 3
        test_data = [gjtk.random.geometry() for _ in range(int(length))]
        test_result = gjtk.generate.geometry_collection(test_data)
        self.assertTrue(
            gjtk.validate.is_geometry_collection(test_result),
            gjtk.test.error_message(test_data, test_result),
        )

    def test_nothing(self):
        """should return a valid GeometryCollection object when provided nothing"""
        test_data = None
        test_result = gjtk.generate.geometry_collection(test_data)
        self.assertTrue(
            gjtk.validate.is_geometry_collection(test_result),
            gjtk.test.error_message(test_data, test_result),
        )


class FeatureTest(unittest.TestCase):

    """Tests for Feature Generation"""

    def test_valid_geometry(self):
        """should return a valid Feature object when provided a valid Geometry"""
        test_data = gjtk.random.geometry()
        test_result = gjtk.generate.feature(test_data)
        self.assertTrue(
            gjtk.validate.is_feature(test_result),
            gjtk.test.error_message(test_data, test_result),
        )


class FeatureCollectionTest(unittest.TestCase):

    """Tests for FeatureCollection Generation"""

    def test_valid_features(self):
        """should return a valid FeatureCollection object when provided valid Features"""
        length = round(random.random() * 100) % 3
        test_data = [gjtk.random.feature() for _ in range(int(length))]
        test_result = gjtk.generate.feature_collection(test_data)
        self.assertTrue(
            gjtk.validate.is_feature_collection(test_result),
            gjtk.test.error_message(test_data, test_result),
        )

    def test_nothing(self):
        """should return a valid FeatureCollection object when provided nothing"""
        test_data = None
        test_result = gjtk.generate.feature_collection(test_data)
        self.assertTrue(
            gjtk.validate.is_feature_collection(test_result),
            gjtk.test.error_message(test_data, test_result),
        )


if __name__ == "__main__":
    unittest.main()
