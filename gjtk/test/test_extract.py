"""Tests for GeoJSON ToolKit Extraction Utilities"""

import unittest

import gjtk


class ExtractPositionsTest(unittest.TestCase):

    """Tests for Position Extraction"""

    def test_valid_point(self):
        """should return valid positions when provided a valid Point"""
        test_data = gjtk.random.point()
        test_result = gjtk.extract.positions_of(test_data)
        self.assertTrue(
            all(gjtk.validate.is_position(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result),
        )

    def test_valid_multi_point(self):
        """should return valid positions when provided a valid MultiPoint"""
        test_data = gjtk.random.multi_point()
        test_result = gjtk.extract.positions_of(test_data)
        self.assertTrue(
            all(gjtk.validate.is_position(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result),
        )

    def test_valid_line_string(self):
        """should return valid positions when provided a valid LineString"""
        test_data = gjtk.random.line_string()
        test_result = gjtk.extract.positions_of(test_data)
        self.assertTrue(
            all(gjtk.validate.is_position(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result),
        )

    def test_valid_multi_line_string(self):
        """should return valid positions when provided a valid MultiLineString"""
        test_data = gjtk.random.multi_line_string()
        test_result = gjtk.extract.positions_of(test_data)
        self.assertTrue(
            all(gjtk.validate.is_position(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result),
        )

    def test_valid_polygon(self):
        """should return valid positions when provided a valid Polygon"""
        test_data = gjtk.random.polygon()
        test_result = gjtk.extract.positions_of(test_data)
        self.assertTrue(
            all(gjtk.validate.is_position(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result),
        )

    def test_valid_multi_polygon(self):
        """should return valid positions when provided a valid MultiPolygon"""
        test_data = gjtk.random.multi_polygon()
        test_result = gjtk.extract.positions_of(test_data)
        self.assertTrue(
            all(gjtk.validate.is_position(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result),
        )

    def test_valid_geometry_collection(self):
        """should return valid positions when provided a valid GeometryCollection"""
        test_data = gjtk.random.geometry_collection()
        test_result = gjtk.extract.positions_of(test_data)
        self.assertTrue(
            all(gjtk.validate.is_position(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result),
        )

    def test_valid_feature(self):
        """should return valid positions when provided a valid Feature"""
        test_data = gjtk.random.feature()
        test_result = gjtk.extract.positions_of(test_data)
        self.assertTrue(
            all(gjtk.validate.is_position(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result),
        )

    def test_valid_feature_collection(self):
        """should return valid positions when provided a valid FeatureCollection"""
        test_data = gjtk.random.feature_collection()
        test_result = gjtk.extract.positions_of(test_data)
        self.assertTrue(
            all(gjtk.validate.is_position(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result),
        )


class ExtractFeaturesTest(unittest.TestCase):

    """Tests for Feature Extraction"""

    def test_valid_feature(self):
        """should return valid features when provided a valid Feature"""
        test_data = gjtk.random.feature()
        test_result = gjtk.extract.features_of(test_data)
        self.assertTrue(
            all(gjtk.validate.is_feature(feature) for feature in test_result),
            gjtk.test.error_message(test_data, test_result),
        )

    def test_valid_feature_collection(self):
        """should return valid features when provided a valid FeatureCollection"""
        test_data = gjtk.random.feature_collection()
        test_result = gjtk.extract.features_of(test_data)
        self.assertTrue(
            all(gjtk.validate.is_feature(feature) for feature in test_result),
            gjtk.test.error_message(test_data, test_result),
        )


class ExtractGeometriesTest(unittest.TestCase):

    """Tests for Geometry Extraction"""

    def test_valid_point(self):
        """should return valid geometries when provided a valid Point"""
        test_data = gjtk.random.point()
        test_result = gjtk.extract.geometries_of(test_data)
        self.assertTrue(
            all(gjtk.validate.is_geometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result),
        )

    def test_valid_multi_point(self):
        """should return valid geometries when provided a valid MultiPoint"""
        test_data = gjtk.random.multi_point()
        test_result = gjtk.extract.geometries_of(test_data)
        self.assertTrue(
            all(gjtk.validate.is_geometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result),
        )

    def test_valid_line_string(self):
        """should return valid geometries when provided a valid LineString"""
        test_data = gjtk.random.line_string()
        test_result = gjtk.extract.geometries_of(test_data)
        self.assertTrue(
            all(gjtk.validate.is_geometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result),
        )

    def test_valid_multi_line_string(self):
        """should return valid geometries when provided a valid MultiLineString"""
        test_data = gjtk.random.multi_line_string()
        test_result = gjtk.extract.geometries_of(test_data)
        self.assertTrue(
            all(gjtk.validate.is_geometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result),
        )

    def test_valid_polygon(self):
        """should return valid geometries when provided a valid Polygon"""
        test_data = gjtk.random.polygon()
        test_result = gjtk.extract.geometries_of(test_data)
        self.assertTrue(
            all(gjtk.validate.is_geometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result),
        )

    def test_valid_multi_polygon(self):
        """should return valid geometries when provided a valid MultiPolygon"""
        test_data = gjtk.random.multi_polygon()
        test_result = gjtk.extract.geometries_of(test_data)
        self.assertTrue(
            all(gjtk.validate.is_geometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result),
        )

    def test_valid_geometry_collection(self):
        """should return valid geometries when provided a valid GeometryCollection"""
        test_data = gjtk.random.geometry_collection()
        test_result = gjtk.extract.geometries_of(test_data)
        self.assertTrue(
            all(gjtk.validate.is_geometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result),
        )

    def test_valid_feature(self):
        """should return valid geometries when provided a valid Feature"""
        test_data = gjtk.random.feature()
        test_result = gjtk.extract.geometries_of(test_data)
        self.assertTrue(
            all(gjtk.validate.is_geometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result),
        )

    def test_valid_feature_collection(self):
        """should return valid geometries when provided a valid FeatureCollection"""
        test_data = gjtk.random.feature_collection()
        test_result = gjtk.extract.geometries_of(test_data)
        self.assertTrue(
            all(gjtk.validate.is_geometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result),
        )


if __name__ == "__main__":
    unittest.main()
