"""Tests for GeoJSON ToolKit Random Generation Utilities"""

import unittest

import gjtk


class PositionTest(unittest.TestCase):

    """Tests for Random Position Generation"""

    def test_position(self):
        """should return a valid Position"""
        test_data = gjtk.random.position(max_numbers=6)
        self.assertTrue(
            gjtk.validate.is_position(test_data),
            gjtk.test.error_message(test_data),
        )


class PointCoordinatesTest(unittest.TestCase):

    """Tests for Random Point Coordinates Generation"""

    def test_point_coordinates(self):
        """should return a valid Point coordinates"""
        test_data = gjtk.random.point_coordinates()
        self.assertTrue(
            gjtk.validate.is_point_coordinates(test_data),
            gjtk.test.error_message(test_data),
        )


class MultiPointCoordinatesTest(unittest.TestCase):

    """Tests for Random MultiPoint Coordinates Generation"""

    def test_multi_point_coordinates(self):
        """should return a valid MultiPoint coordinates"""
        test_data = gjtk.random.multi_point_coordinates()
        self.assertTrue(
            gjtk.validate.is_multi_point_coordinates(test_data),
            gjtk.test.error_message(test_data),
        )


class LineStringCoordinatesTest(unittest.TestCase):

    """Tests for Random LineString Coordinates Generation"""

    def test_line_string_coordinates(self):
        """should return a valid LineString coordinates"""
        test_data = gjtk.random.line_string_coordinates()
        self.assertTrue(
            gjtk.validate.is_line_string_coordinates(test_data),
            gjtk.test.error_message(test_data),
        )


class LinearRingCoordinatesTest(unittest.TestCase):

    """Tests for Random LinearRing Coordinates Generation"""

    def test_linear_ring_coordinates(self):
        """should return a valid LinearRing coordinates"""
        test_data = gjtk.random.linear_ring_coordinates()
        self.assertTrue(
            gjtk.validate.is_linear_ring_coordinates(test_data),
            gjtk.test.error_message(test_data),
        )


class MultiLineStringCoordinatesTest(unittest.TestCase):

    """Tests for Random MultiLineString Coordinates Generation"""

    def test_multi_line_string_coordinates(self):  # pylint: disable=invalid-name
        """should return a valid MultiLineString coordinates"""
        test_data = gjtk.random.multi_line_string_coordinates()
        self.assertTrue(
            gjtk.validate.is_multi_line_string_coordinates(test_data),
            gjtk.test.error_message(test_data),
        )


class PolygonCoordinatesTest(unittest.TestCase):

    """Tests for Random Polygon Coordinates Generation"""

    def test_polygon_coordinates(self):
        """should return a valid Polygon coordinates"""
        test_data = gjtk.random.polygon_coordinates()
        self.assertTrue(
            gjtk.validate.is_polygon_coordinates(test_data),
            gjtk.test.error_message(test_data),
        )


class MultiPolygonCoordinatesTest(unittest.TestCase):

    """Tests for Random MultiPolygon Coordinates Generation"""

    def test_multi_polygon_coordinates(self):
        """should return a valid MultiPolygon coordinates"""
        test_data = gjtk.random.multi_polygon_coordinates()
        self.assertTrue(
            gjtk.validate.is_multi_polygon_coordinates(test_data),
            gjtk.test.error_message(test_data),
        )


class GeometryTest(unittest.TestCase):

    """Tests for Random Geometry Generation"""

    def test_geometry(self):
        """should return a valid Geometry"""
        test_data = gjtk.random.geometry()
        self.assertTrue(
            gjtk.validate.is_geometry(test_data),
            gjtk.test.error_message(test_data),
        )


class PointTest(unittest.TestCase):

    """Tests for Random Point Generation"""

    def test_point(self):
        """should return a valid Point"""
        test_data = gjtk.random.point()
        self.assertTrue(
            gjtk.validate.is_point(test_data),
            gjtk.test.error_message(test_data),
        )


class MultiPointTest(unittest.TestCase):

    """Tests for Random MultiPoint Generation"""

    def test_multi_point(self):
        """should return a valid MultiPoint"""
        test_data = gjtk.random.multi_point()
        self.assertTrue(
            gjtk.validate.is_multi_point(test_data),
            gjtk.test.error_message(test_data),
        )


class LineStringTest(unittest.TestCase):

    """Tests for Random LineString Generation"""

    def test_line_string(self):
        """should return a valid LineString"""
        test_data = gjtk.random.line_string()
        self.assertTrue(
            gjtk.validate.is_line_string(test_data),
            gjtk.test.error_message(test_data),
        )


class MultiLineStringTest(unittest.TestCase):

    """Tests for Random MultiLineString Generation"""

    def test_multi_line_string(self):
        """should return a valid MultiLineString"""
        test_data = gjtk.random.multi_line_string()
        self.assertTrue(
            gjtk.validate.is_multi_line_string(test_data),
            gjtk.test.error_message(test_data),
        )


class PolygonTest(unittest.TestCase):

    """Tests for Random Polygon Generation"""

    def test_polygon(self):
        """should return a valid Polygon"""
        test_data = gjtk.random.polygon()
        self.assertTrue(
            gjtk.validate.is_polygon(test_data),
            gjtk.test.error_message(test_data),
        )


class MultiPolygonTest(unittest.TestCase):

    """Tests for Random MultiPolygon Generation"""

    def test_multi_polygon(self):
        """should return a valid MultiPolygon"""
        test_data = gjtk.random.multi_polygon()
        self.assertTrue(
            gjtk.validate.is_multi_polygon(test_data),
            gjtk.test.error_message(test_data),
        )


class GeometryCollectionTest(unittest.TestCase):

    """Tests for Random GeometryCollection Generation"""

    def test_geometry_collection(self):
        """should return a valid GeometryCollection"""
        test_data = gjtk.random.geometry_collection()
        self.assertTrue(
            gjtk.validate.is_geometry_collection(test_data),
            gjtk.test.error_message(test_data),
        )


class FeatureTest(unittest.TestCase):

    """Tests for Random Feature Generation"""

    def test_feature(self):
        """should return a valid Feature"""
        test_data = gjtk.random.feature()
        self.assertTrue(
            gjtk.validate.is_feature(test_data),
            gjtk.test.error_message(test_data),
        )


class FeatureCollectionTest(unittest.TestCase):

    """Tests for Random FeatureCollection Generation"""

    def test_feature_collection(self):
        """should return a valid FeatureCollection"""
        test_data = gjtk.random.feature_collection()
        self.assertTrue(
            gjtk.validate.is_feature_collection(test_data),
            gjtk.test.error_message(test_data),
        )


class CRSTest(unittest.TestCase):

    """Tests for Random CRS Generation"""

    def test_crs(self):
        """should return a valid CRS"""
        test_data = gjtk.random.crs()
        self.assertTrue(
            gjtk.validate.is_crs(test_data),
            gjtk.test.error_message(test_data),
        )


class LinkTest(unittest.TestCase):

    """Tests for Random Link Generation"""

    def test_link(self):
        """should return a valid Link"""
        test_data = gjtk.random.link()
        self.assertTrue(
            gjtk.validate.is_link(test_data),
            gjtk.test.error_message(test_data),
        )


class BBoxTest(unittest.TestCase):

    """Tests for Random BBox Generation"""

    def test_bbox(self):
        """should return a valid Bbox"""
        test_data = gjtk.random.bbox()
        self.assertTrue(
            gjtk.validate.is_bbox(test_data),
            gjtk.test.error_message(test_data),
        )


if __name__ == "__main__":
    unittest.main()
