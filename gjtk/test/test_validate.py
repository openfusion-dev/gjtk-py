"""Tests for GeoJSON ToolKit Validation Utilities"""

import random
import unittest

import gjtk


class GeoJSONTest(unittest.TestCase):

    """Tests for GeoJSON Validation"""

    def test_geometry(self):
        """should return true when provided a valid Geometry object"""
        test_data = gjtk.random.geometry()
        self.assertTrue(
            gjtk.validate.is_geojson(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_feature(self):
        """should return true when provided a valid Feature object"""
        test_data = gjtk.random.feature()
        self.assertTrue(
            gjtk.validate.is_geojson(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_feature_collection(self):
        """should return true when provided a valid Feature object"""
        test_data = gjtk.random.feature_collection()
        self.assertTrue(
            gjtk.validate.is_geojson(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.is_geojson(test_data),
            gjtk.test.error_message(test_data),
        )


class GeometryTest(unittest.TestCase):

    """Tests for Geometry Validation"""

    def test_point(self):
        """should return true when provided a valid Point object"""
        test_data = gjtk.random.point()
        self.assertTrue(
            gjtk.validate.is_geometry(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_multi_point(self):
        """should return true when provided a valid MultiPoint object"""
        test_data = gjtk.random.multi_point()
        self.assertTrue(
            gjtk.validate.is_geometry(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_line_string(self):
        """should return true when provided a valid LineString object"""
        test_data = gjtk.random.line_string()
        self.assertTrue(
            gjtk.validate.is_geometry(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_multi_line_string(self):
        """should return true when provided a valid MultiLineString object"""
        test_data = gjtk.random.multi_line_string()
        self.assertTrue(
            gjtk.validate.is_geometry(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_polygon(self):
        """should return true when provided a valid Polygon object"""
        test_data = gjtk.random.polygon()
        self.assertTrue(
            gjtk.validate.is_geometry(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_multi_polygon(self):
        """should return true when provided a valid MultiPolygon object"""
        test_data = gjtk.random.multi_polygon()
        self.assertTrue(
            gjtk.validate.is_geometry(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_geometry_collection(self):
        """should return true when provided a valid GeometryCollection object"""
        test_data = gjtk.random.geometry_collection()
        self.assertTrue(
            gjtk.validate.is_geometry(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.is_geometry(test_data),
            gjtk.test.error_message(test_data),
        )


class PositionTest(unittest.TestCase):

    """Tests for Position Validation"""

    def test_position(self):
        """should return true when provided an array of at least 2 numbers"""
        test_data = gjtk.random.position(max_numbers=6)
        self.assertTrue(
            gjtk.validate.is_position(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_too_short(self):
        """should return false when provided an array of less than 2 numbers"""
        test_data = [1]
        self.assertFalse(
            gjtk.validate.is_position(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_incorrect_type(self):
        """should return false when provided an array of at least 2 non-numbers"""
        test_data = ['foo', 'bar']
        self.assertFalse(
            gjtk.validate.is_position(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_mixed_types(self):
        """
        should return false when provided an array of a mix of at least 2 numbers and non-numbers
        """
        test_data = [1, 'a']
        random.shuffle(test_data)
        self.assertFalse(
            gjtk.validate.is_position(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.is_position(test_data),
            gjtk.test.error_message(test_data),
        )


class PointCoordinatesTest(unittest.TestCase):

    """Tests for Point Coordinates Validation"""

    def test_point_coordinates(self):
        """should return true when provided valid GeoJSON Point coordinates"""
        test_data = gjtk.random.point_coordinates()
        self.assertTrue(
            gjtk.validate.is_point_coordinates(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.is_point_coordinates(test_data),
            gjtk.test.error_message(test_data),
        )


class MultiPointCoordinatesTest(unittest.TestCase):

    """Tests for MultiPoint Coordinates Validation"""

    def test_multi_point_coordinates(self):
        """should return true when provided valid GeoJSON MultiPoint coordinates"""
        test_data = gjtk.random.multi_point_coordinates()
        self.assertTrue(
            gjtk.validate.is_multi_point_coordinates(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            {},
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.is_multi_point_coordinates(test_data),
            gjtk.test.error_message(test_data),
        )


class LineStringCoordinatesTest(unittest.TestCase):

    """Tests for LineString Coordinates Validation"""

    def test_line_string_coordinates(self):
        """should return true when provided valid GeoJSON LineString coordinates"""
        test_data = gjtk.random.line_string_coordinates()
        self.assertTrue(
            gjtk.validate.is_line_string_coordinates(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            {},
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.is_line_string_coordinates(test_data),
            gjtk.test.error_message(test_data),
        )


class LinearRingCoordinatesTest(unittest.TestCase):

    """Tests for LinearRing Coordinates Validation"""

    def test_linear_ring_coordinates(self):
        """should return true when provided a valid GeoJSON LinearRing"""
        test_data = gjtk.random.linear_ring_coordinates()
        self.assertTrue(
            gjtk.validate.is_linear_ring_coordinates(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            {},
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.is_linear_ring_coordinates(test_data),
            gjtk.test.error_message(test_data),
        )


class MultiLineStringCoordinatesTest(unittest.TestCase):

    """Tests for MultiLineString Coordinates Validation"""

    def test_multi_line_string_coordinates(self):  # pylint: disable=invalid-name
        """should return true when provided valid GeoJSON MultiLineString coordinates"""
        test_data = gjtk.random.multi_line_string_coordinates()
        self.assertTrue(
            gjtk.validate.is_multi_line_string_coordinates(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            {},
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.is_multi_line_string_coordinates(test_data),
            gjtk.test.error_message(test_data),
        )


class PolygonCoordinatesTest(unittest.TestCase):

    """Tests for Polygon Coordinates Validation"""

    def test_polygon_coordinates(self):
        """should return true when provided valid GeoJSON Polygon coordinates"""
        test_data = gjtk.random.polygon_coordinates()
        self.assertTrue(
            gjtk.validate.is_polygon_coordinates(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            {},
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.is_polygon_coordinates(test_data),
            gjtk.test.error_message(test_data),
        )


class MultiPolygonCoordinatesTest(unittest.TestCase):

    """Tests for MultiPolygon Coordinates Validation"""

    def test_multi_polygon_coordinates(self):
        """should return true when provided valid GeoJSON MultiPolygon coordinates"""
        test_data = gjtk.random.multi_polygon_coordinates()
        self.assertTrue(
            gjtk.validate.is_multi_polygon_coordinates(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            {},
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.is_multi_polygon_coordinates(test_data),
            gjtk.test.error_message(test_data),
        )


class PointTest(unittest.TestCase):

    """Tests for Point Validation"""

    def test_point(self):
        """should return true when provided a valid Point object"""
        test_data = gjtk.random.point()
        self.assertTrue(
            gjtk.validate.is_point(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_no_type(self):
        """should return false when provided a Point object without a type"""
        test_data = gjtk.random.point()
        del test_data['type']
        self.assertFalse(
            gjtk.validate.is_point(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_no_coordinates(self):
        """should return false when provided a Point object without coordinates"""
        test_data = gjtk.random.point()
        del test_data['coordinates']
        self.assertFalse(
            gjtk.validate.is_point(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.is_point(test_data),
            gjtk.test.error_message(test_data),
        )


class MultiPointTest(unittest.TestCase):

    """Tests for MultiPoint Validation"""

    def test_multi_point(self):
        """should return true when provided a valid MultiPoint object"""
        test_data = gjtk.random.multi_point()
        self.assertTrue(
            gjtk.validate.is_multi_point(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_no_type(self):
        """should return false when provided a MultiPoint object without a type"""
        test_data = gjtk.random.multi_point()
        del test_data['type']
        self.assertFalse(
            gjtk.validate.is_multi_point(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_no_coordinates(self):
        """should return false when provided a MultiPoint object without coordinates"""
        test_data = gjtk.random.multi_point()
        del test_data['coordinates']
        self.assertFalse(
            gjtk.validate.is_multi_point(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.is_multi_point(test_data),
            gjtk.test.error_message(test_data),
        )


class LineStringTest(unittest.TestCase):

    """Tests for LineString Validation"""

    def test_line_string(self):
        """should return true when provided a valid LineString object"""
        test_data = gjtk.random.line_string()
        self.assertTrue(
            gjtk.validate.is_line_string(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_no_type(self):
        """should return false when provided a LineString object without a type"""
        test_data = gjtk.random.line_string()
        del test_data['type']
        self.assertFalse(
            gjtk.validate.is_line_string(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_no_coordinates(self):
        """should return false when provided a LineString object without coordinates"""
        test_data = gjtk.random.line_string()
        del test_data['coordinates']
        self.assertFalse(
            gjtk.validate.is_line_string(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.is_line_string(test_data),
            gjtk.test.error_message(test_data),
        )


class MultiLineStringTest(unittest.TestCase):

    """Tests for MultiLineString Validation"""

    def test_multi_line_string(self):
        """should return true when provided a valid MultiLineString object"""
        test_data = gjtk.random.multi_line_string()
        self.assertTrue(
            gjtk.validate.is_multi_line_string(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_no_type(self):
        """should return false when provided a MultiLineString object without a type"""
        test_data = gjtk.random.multi_line_string()
        del test_data['type']
        self.assertFalse(
            gjtk.validate.is_multi_line_string(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_no_coordinates(self):
        """should return false when provided a MultiLineString object without coordinates"""
        test_data = gjtk.random.multi_line_string()
        del test_data['coordinates']
        self.assertFalse(
            gjtk.validate.is_multi_line_string(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.is_multi_line_string(test_data),
            gjtk.test.error_message(test_data),
        )


class PolygonTest(unittest.TestCase):

    """Tests for Polygon Validation"""

    def test_polygon(self):
        """should return true when provided a valid Polygon object"""
        test_data = gjtk.random.polygon()
        self.assertTrue(
            gjtk.validate.is_polygon(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_no_type(self):
        """should return false when provided a Polygon object without a type"""
        test_data = gjtk.random.polygon()
        del test_data['type']
        self.assertFalse(
            gjtk.validate.is_polygon(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_no_coordinates(self):
        """should return false when provided a Polygon object without coordinates"""
        test_data = gjtk.random.polygon()
        del test_data['coordinates']
        self.assertFalse(
            gjtk.validate.is_polygon(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.is_polygon(test_data),
            gjtk.test.error_message(test_data),
        )


class MultiPolygonTest(unittest.TestCase):

    """Tests for MultiPolygon Validation"""

    def test_multi_polygon(self):
        """should return true when provided a valid MultiPolygon object"""
        test_data = gjtk.random.multi_polygon()
        self.assertTrue(
            gjtk.validate.is_multi_polygon(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_no_type(self):
        """should return false when provided a MultiPolygon object without a type"""
        test_data = gjtk.random.multi_polygon()
        del test_data['type']
        self.assertFalse(
            gjtk.validate.is_multi_polygon(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_no_coordinates(self):
        """should return false when provided a MultiPolygon object without coordinates"""
        test_data = gjtk.random.multi_polygon()
        del test_data['coordinates']
        self.assertFalse(
            gjtk.validate.is_multi_polygon(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.is_multi_polygon(test_data),
            gjtk.test.error_message(test_data),
        )


class GeometryCollectionTest(unittest.TestCase):

    """Tests for GeometryCollection Validation"""

    def test_geometry_collection(self):
        """should return true when provided a valid GeometryCollection object"""
        test_data = gjtk.random.geometry_collection()
        self.assertTrue(
            gjtk.validate.is_geometry_collection(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_no_type(self):
        """should return false when provided a GeometryCollection object without a type"""
        test_data = gjtk.random.geometry_collection()
        del test_data['type']
        self.assertFalse(
            gjtk.validate.is_geometry_collection(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_no_geometries(self):
        """should return false when provided a GeometryCollection object without geometries"""
        test_data = gjtk.random.geometry_collection()
        del test_data['geometries']
        self.assertFalse(
            gjtk.validate.is_geometry_collection(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.is_geometry_collection(test_data),
            gjtk.test.error_message(test_data),
        )


class FeatureTest(unittest.TestCase):

    """Tests for Feature Validation"""

    def test_feature(self):
        """should return true when provided a valid Feature object"""
        test_data = gjtk.random.feature()
        self.assertTrue(
            gjtk.validate.is_feature(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_no_type(self):
        """should return false when provided a Feature object without a type"""
        test_data = gjtk.random.feature()
        del test_data['type']
        self.assertFalse(
            gjtk.validate.is_feature(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_no_geometry(self):
        """should return false when provided a Feature object without geometry"""
        test_data = gjtk.random.feature()
        del test_data['geometry']
        self.assertFalse(
            gjtk.validate.is_feature(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.is_feature(test_data),
            gjtk.test.error_message(test_data),
        )


class FeatureCollectionTest(unittest.TestCase):

    """Tests for FeatureCollection Validation"""

    def test_feature_collection(self):
        """should return true when provided a valid FeatureCollection object"""
        test_data = gjtk.random.feature_collection()
        self.assertTrue(
            gjtk.validate.is_feature_collection(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_no_type(self):
        """should return false when provided a FeatureCollection object without a type"""
        test_data = gjtk.random.feature_collection()
        del test_data['type']
        self.assertFalse(
            gjtk.validate.is_feature_collection(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_no_features(self):
        """should return false when provided a FeatureCollection object without features"""
        test_data = gjtk.random.feature_collection()
        del test_data['features']
        self.assertFalse(
            gjtk.validate.is_feature_collection(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.is_feature_collection(test_data),
            gjtk.test.error_message(test_data),
        )


class CRSTest(unittest.TestCase):

    """Tests for CRS Validation"""

    def test_crs(self):
        """should return true when provided a valid CRS object"""
        test_data = gjtk.random.crs()
        self.assertTrue(
            gjtk.validate.is_crs(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_no_type(self):
        """should return false when provided a CRS object without a type"""
        test_data = gjtk.random.crs()
        del test_data['type']
        self.assertFalse(
            gjtk.validate.is_crs(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_no_properties(self):
        """should return false when provided a CRS object without properties"""
        test_data = gjtk.random.crs()
        del test_data['properties']
        self.assertFalse(
            gjtk.validate.is_crs(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.is_crs(test_data),
            gjtk.test.error_message(test_data),
        )


class HasCRSTest(unittest.TestCase):

    """Tests for CRS Presence Validation"""

    def test_geometry_crs(self):
        """should return true when provided a Geometry with a valid CRS"""
        test_data = gjtk.random.geometry()
        test_data['crs'] = gjtk.random.crs()
        self.assertTrue(
            gjtk.validate.has_bbox(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_feature_crs(self):
        """should return true when provided a Feature with a valid CRS"""
        test_data = gjtk.random.feature()
        test_data['crs'] = gjtk.random.crs()
        self.assertTrue(
            gjtk.validate.has_bbox(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_feature_collection_crs(self):
        """should return true when provided a FeatureCollection with a valid CRS"""
        test_data = gjtk.random.feature_collection()
        test_data['crs'] = gjtk.random.crs()
        self.assertTrue(
            gjtk.validate.has_bbox(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            [],
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.has_crs(test_data),
            gjtk.test.error_message(test_data),
        )


class LinkTest(unittest.TestCase):

    """Tests for Link Validation"""

    def test_link(self):
        """should return true when provided a valid Link object"""
        test_data = gjtk.random.link()
        self.assertTrue(
            gjtk.validate.is_link(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_no_type(self):
        """should return true when provided a Link object without a type"""
        test_data = gjtk.random.link()
        if 'type' in test_data:
            del test_data['type']
        self.assertTrue(
            gjtk.validate.is_link(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_no_href(self):
        """should return false when provided a Link object without href"""
        test_data = gjtk.random.link()
        del test_data['href']
        self.assertFalse(
            gjtk.validate.is_link(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.is_link(test_data),
            gjtk.test.error_message(test_data),
        )


class BBoxTest(unittest.TestCase):

    """Tests for BBox Validation"""

    def test_bbox(self):
        """should return true when provided a valid Bbox"""
        test_data = gjtk.random.bbox()
        self.assertTrue(
            gjtk.validate.is_bbox(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.is_bbox(test_data),
            gjtk.test.error_message(test_data),
        )


class HasBboxTest(unittest.TestCase):

    """Tests for BBox Presence Validation"""

    def test_geometry_bbox(self):
        """should return true when provided a Geometry with a valid Bbox"""
        test_data = gjtk.random.geometry()
        test_data['bbox'] = gjtk.random.bbox()
        self.assertTrue(
            gjtk.validate.has_bbox(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_feature_bbox(self):
        """should return true when provided a Feature with a valid Bbox"""
        test_data = gjtk.random.feature()
        test_data['bbox'] = gjtk.random.bbox()
        self.assertTrue(
            gjtk.validate.has_bbox(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_feature_collection_bbox(self):
        """should return true when provided a FeatureCollection with a valid Bbox"""
        test_data = gjtk.random.feature_collection()
        test_data['bbox'] = gjtk.random.bbox()
        self.assertTrue(
            gjtk.validate.has_bbox(test_data),
            gjtk.test.error_message(test_data),
        )

    def test_invalid(self):
        """should return false when provided an invalid object"""
        test_data = random.choice([
            True,
            0,
            '',
            [],
            random.choice,
            None,
        ])
        self.assertFalse(
            gjtk.validate.has_bbox(test_data),
            gjtk.test.error_message(test_data),
        )


# COMPARISON


class EqualPositionsTest(unittest.TestCase):

    """Tests for Position Equality Validation"""

    def test_same(self):
        """should return true when provided identical Positions"""
        test_data = gjtk.random.position(max_numbers=6)
        self.assertTrue(
            gjtk.validate.equal_positions(test_data, test_data),
            gjtk.test.error_message(test_data),
        )

    def test_diff(self):
        """should return false when provided different Positions"""
        test_data1 = gjtk.random.position(max_numbers=6)
        test_data2 = gjtk.random.position(max_numbers=6)
        while test_data1[0] == test_data2[0]:
            gjtk.random.position(max_numbers=6)
        self.assertFalse(
            gjtk.validate.equal_positions(test_data1, test_data2),
            gjtk.test.error_message([test_data1, test_data2]),
        )


class ContainedPolygonTest(unittest.TestCase):

    """Tests for Containg Polygon Validation"""

    def setUp(self):
        self.inner = [[1, 1], [1, 2], [2, 2], [2, 1], [1, 1]]
        self.outer = [[0, 0], [0, 5], [5, 5], [5, 0], [0, 0]]

    def test_contained(self):
        """should return true when provided a LinearRing that contains another LinearRing."""
        self.assertTrue(gjtk.validate.contained_polygon(self.inner, self.outer))

    def test_not_contained(self):
        """
        should return false when provided a LinearRing that does not contain another LinearRing.
        """
        self.assertFalse(gjtk.validate.contained_polygon(self.outer, self.inner))


# pylint: disable=too-many-lines
if __name__ == "__main__":
    unittest.main()
