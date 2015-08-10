

import random
import unittest

import gjtk


class isGeoJSONTest (unittest.TestCase):

    def test_valid_Geometry(self):
        """ should return true when provided a valid Geometry object """
        test_data = gjtk.random.Geometry()
        self.assertTrue(
            gjtk.validate.isGeoJSON(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_valid_Feature(self):
        """ should return true when provided a valid Feature object """
        test_data = gjtk.random.Feature()
        self.assertTrue(
            gjtk.validate.isGeoJSON(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_valid_FeatureCollection(self):
        """ should return true when provided a valid Feature object """
        test_data = gjtk.random.FeatureCollection()
        self.assertTrue(
            gjtk.validate.isGeoJSON(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.isGeoJSON(test_data),
            gjtk.test.error_message(test_data)
        )


class isGeometryTest (unittest.TestCase):

    def test_valid_Point(self):
        """ should return true when provided a valid Point object """
        test_data = gjtk.random.Point()
        self.assertTrue(
            gjtk.validate.isGeometry(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_valid_MultiPoint(self):
        """ should return true when provided a valid MultiPoint object """
        test_data = gjtk.random.MultiPoint()
        self.assertTrue(
            gjtk.validate.isGeometry(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_valid_LineString(self):
        """ should return true when provided a valid LineString object """
        test_data = gjtk.random.LineString()
        self.assertTrue(
            gjtk.validate.isGeometry(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_valid_MultiLineString(self):
        """ should return true when provided a valid MultiLineString object """
        test_data = gjtk.random.MultiLineString()
        self.assertTrue(
            gjtk.validate.isGeometry(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_valid_Polygon(self):
        """ should return true when provided a valid Polygon object """
        test_data = gjtk.random.Polygon()
        self.assertTrue(
            gjtk.validate.isGeometry(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_valid_MultiPolygon(self):
        """ should return true when provided a valid MultiPolygon object """
        test_data = gjtk.random.MultiPolygon()
        self.assertTrue(
            gjtk.validate.isGeometry(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_valid_GeometryCollection(self):
        """ should return true when provided a valid GeometryCollection object """
        test_data = gjtk.random.GeometryCollection()
        self.assertTrue(
            gjtk.validate.isGeometry(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.isGeometry(test_data),
            gjtk.test.error_message(test_data)
        )


class isPositionTest (unittest.TestCase):

    def test_valid_Position(self):
        """ should return true when provided an array of at least 2 numbers """
        test_data = gjtk.random.Position(max_numbers=6)
        self.assertTrue(
            gjtk.validate.isPosition(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_too_short(self):
        """ should return false when provided an array of less than 2 numbers """
        test_data = [1]
        self.assertFalse(
            gjtk.validate.isPosition(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_incorrect_type(self):
        """ should return false when provided an array of at least 2 non-numbers """
        test_data = ['foo', 'bar']
        self.assertFalse(
            gjtk.validate.isPosition(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_mixed_types(self):
        """ should return false when provided an array of a mix of at least 2 numbers and non-numbers """
        test_data = [1, 'a']
        random.shuffle(test_data)
        self.assertFalse(
            gjtk.validate.isPosition(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.isPosition(test_data),
            gjtk.test.error_message(test_data)
        )


class isPointCoordinatesTest (unittest.TestCase):

    def test_valid_Point_coordinates(self):
        """ should return true when provided valid GeoJSON Point coordinates """
        test_data = gjtk.random.PointCoordinates()
        self.assertTrue(
            gjtk.validate.isPointCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.isPointCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )


class isMultiPointCoordinatesTest (unittest.TestCase):

    def test_valid_MultiPoint_coordinates(self):
        """ should return true when provided valid GeoJSON MultiPoint coordinates """
        test_data = gjtk.random.MultiPointCoordinates()
        self.assertTrue(
            gjtk.validate.isMultiPointCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.isMultiPointCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )


class isLineStringCoordinatesTest (unittest.TestCase):

    def test_valid_LineString_coordinates(self):
        """ should return true when provided valid GeoJSON LineString coordinates """
        test_data = gjtk.random.LineStringCoordinates()
        self.assertTrue(
            gjtk.validate.isLineStringCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.isLineStringCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )


class isLinearRingCoordinatesTest (unittest.TestCase):

    def test_valid_LinearRing_coordinates(self):
        """ should return true when provided a valid GeoJSON LinearRing """
        test_data = gjtk.random.LinearRingCoordinates()
        self.assertTrue(
            gjtk.validate.isLinearRingCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.isLinearRingCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )


class isMultiLineStringCoordinatesTest (unittest.TestCase):

    def test_valid_MultiLineString_coordinates(self):
        """ should return true when provided valid GeoJSON MultiLineString coordinates """
        test_data = gjtk.random.MultiLineStringCoordinates()
        self.assertTrue(
            gjtk.validate.isMultiLineStringCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.isMultiLineStringCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )


class isPolygonCoordinatesTest (unittest.TestCase):

    def test_valid_Polygon_coordinates(self):
        """ should return true when provided valid GeoJSON Polygon coordinates """
        test_data = gjtk.random.PolygonCoordinates()
        self.assertTrue(
            gjtk.validate.isPolygonCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.isPolygonCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )


class isMultiPolygonCoordinatesTest (unittest.TestCase):

    def test_valid_MultiPolygon_coordinates(self):
        """ should return true when provided valid GeoJSON MultiPolygon coordinates """
        test_data = gjtk.random.MultiPolygonCoordinates()
        self.assertTrue(
            gjtk.validate.isMultiPolygonCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.isMultiPolygonCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )


class isPointTest (unittest.TestCase):

    def test_valid_Point(self):
        """ should return true when provided a valid Point object """
        test_data = gjtk.random.Point()
        self.assertTrue(
            gjtk.validate.isPoint(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_no_type(self):
        """ should return false when provided a Point object without a type """
        test_data = gjtk.random.Point()
        del test_data['type']
        self.assertFalse(
            gjtk.validate.isPoint(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_no_coordinates(self):
        """ should return false when provided a Point object without coordinates """
        test_data = gjtk.random.Point()
        del test_data['coordinates']
        self.assertFalse(
            gjtk.validate.isPoint(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.isPoint(test_data),
            gjtk.test.error_message(test_data)
        )


class isMultiPointTest (unittest.TestCase):

    def test_valid_MultiPoint(self):
        """ should return true when provided a valid MultiPoint object """
        test_data = gjtk.random.MultiPoint()
        self.assertTrue(
            gjtk.validate.isMultiPoint(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_no_type(self):
        """ should return false when provided a MultiPoint object without a type """
        test_data = gjtk.random.MultiPoint()
        del test_data['type']
        self.assertFalse(
            gjtk.validate.isMultiPoint(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_no_coordinates(self):
        """ should return false when provided a MultiPoint object without coordinates """
        test_data = gjtk.random.MultiPoint()
        del test_data['coordinates']
        self.assertFalse(
            gjtk.validate.isMultiPoint(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.isMultiPoint(test_data),
            gjtk.test.error_message(test_data)
        )


class isLineStringTest (unittest.TestCase):

    def test_valid_LineString(self):
        """ should return true when provided a valid LineString object """
        test_data = gjtk.random.LineString()
        self.assertTrue(
            gjtk.validate.isLineString(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_no_type(self):
        """ should return false when provided a LineString object without a type """
        test_data = gjtk.random.LineString()
        del test_data['type']
        self.assertFalse(
            gjtk.validate.isLineString(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_no_coordinates(self):
        """ should return false when provided a LineString object without coordinates """
        test_data = gjtk.random.LineString()
        del test_data['coordinates']
        self.assertFalse(
            gjtk.validate.isLineString(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.isLineString(test_data),
            gjtk.test.error_message(test_data)
        )


class isMultiLineStringTest (unittest.TestCase):

    def test_valid_MultiLineString(self):
        """ should return true when provided a valid MultiLineString object """
        test_data = gjtk.random.MultiLineString()
        self.assertTrue(
            gjtk.validate.isMultiLineString(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_no_type(self):
        """ should return false when provided a MultiLineString object without a type """
        test_data = gjtk.random.MultiLineString()
        del test_data['type']
        self.assertFalse(
            gjtk.validate.isMultiLineString(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_no_coordinates(self):
        """ should return false when provided a MultiLineString object without coordinates """
        test_data = gjtk.random.MultiLineString()
        del test_data['coordinates']
        self.assertFalse(
            gjtk.validate.isMultiLineString(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.isMultiLineString(test_data),
            gjtk.test.error_message(test_data)
        )


class isPolygonTest (unittest.TestCase):

    def test_valid_Polygon(self):
        """ should return true when provided a valid Polygon object """
        test_data = gjtk.random.Polygon()
        self.assertTrue(
            gjtk.validate.isPolygon(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_no_type(self):
        """ should return false when provided a Polygon object without a type """
        test_data = gjtk.random.Polygon()
        del test_data['type']
        self.assertFalse(
            gjtk.validate.isPolygon(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_no_coordinates(self):
        """ should return false when provided a Polygon object without coordinates """
        test_data = gjtk.random.Polygon()
        del test_data['coordinates']
        self.assertFalse(
            gjtk.validate.isPolygon(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.isPolygon(test_data),
            gjtk.test.error_message(test_data)
        )


class isMultiPolygonTest (unittest.TestCase):

    def test_valid_MultiPolygon(self):
        """ should return true when provided a valid MultiPolygon object """
        test_data = gjtk.random.MultiPolygon()
        self.assertTrue(
            gjtk.validate.isMultiPolygon(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_no_type(self):
        """ should return false when provided a MultiPolygon object without a type """
        test_data = gjtk.random.MultiPolygon()
        del test_data['type']
        self.assertFalse(
            gjtk.validate.isMultiPolygon(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_no_coordinates(self):
        """ should return false when provided a MultiPolygon object without coordinates """
        test_data = gjtk.random.MultiPolygon()
        del test_data['coordinates']
        self.assertFalse(
            gjtk.validate.isMultiPolygon(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.isMultiPolygon(test_data),
            gjtk.test.error_message(test_data)
        )


class isGeometryCollectionTest (unittest.TestCase):

    def test_valid_GeometryCollection(self):
        """ should return true when provided a valid GeometryCollection object """
        test_data = gjtk.random.GeometryCollection()
        self.assertTrue(
            gjtk.validate.isGeometryCollection(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_no_type(self):
        """ should return false when provided a GeometryCollection object without a type """
        test_data = gjtk.random.GeometryCollection()
        del test_data['type']
        self.assertFalse(
            gjtk.validate.isGeometryCollection(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_no_geometries(self):
        """ should return false when provided a GeometryCollection object without geometries """
        test_data = gjtk.random.GeometryCollection()
        del test_data['geometries']
        self.assertFalse(
            gjtk.validate.isGeometryCollection(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.isGeometryCollection(test_data),
            gjtk.test.error_message(test_data)
        )


class isFeatureTest (unittest.TestCase):

    def test_valid_Feature(self):
        """ should return true when provided a valid Feature object """
        test_data = gjtk.random.Feature()
        self.assertTrue(
            gjtk.validate.isFeature(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_no_type(self):
        """ should return false when provided a Feature object without a type """
        test_data = gjtk.random.Feature()
        del test_data['type']
        self.assertFalse(
            gjtk.validate.isFeature(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_no_geometry(self):
        """ should return false when provided a Feature object without geometry """
        test_data = gjtk.random.Feature()
        del test_data['geometry']
        self.assertFalse(
            gjtk.validate.isFeature(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.isFeature(test_data),
            gjtk.test.error_message(test_data)
        )


class isFeatureCollectionTest (unittest.TestCase):

    def test_valid_FeatureCollection(self):
        """ should return true when provided a valid FeatureCollection object """
        test_data = gjtk.random.FeatureCollection()
        self.assertTrue(
            gjtk.validate.isFeatureCollection(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_no_type(self):
        """ should return false when provided a FeatureCollection object without a type """
        test_data = gjtk.random.FeatureCollection()
        del test_data['type']
        self.assertFalse(
            gjtk.validate.isFeatureCollection(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_no_features(self):
        """ should return false when provided a FeatureCollection object without features """
        test_data = gjtk.random.FeatureCollection()
        del test_data['features']
        self.assertFalse(
            gjtk.validate.isFeatureCollection(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.isFeatureCollection(test_data),
            gjtk.test.error_message(test_data)
        )


class isCRSTest (unittest.TestCase):

    def test_valid_CRS(self):
        """ should return true when provided a valid CRS object """
        test_data = gjtk.random.CRS()
        self.assertTrue(
            gjtk.validate.isCRS(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_no_type(self):
        """ should return false when provided a CRS object without a type """
        test_data = gjtk.random.CRS()
        del test_data['type']
        self.assertFalse(
            gjtk.validate.isCRS(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_no_properties(self):
        """ should return false when provided a CRS object without properties """
        test_data = gjtk.random.CRS()
        del test_data['properties']
        self.assertFalse(
            gjtk.validate.isCRS(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.isCRS(test_data),
            gjtk.test.error_message(test_data)
        )


class hasCRSTest (unittest.TestCase):

    def test_valid_Geometry_CRS(self):
        """ should return true when provided a Geometry with a valid CRS """
        test_data = gjtk.random.Geometry()
        test_data['crs'] = gjtk.random.CRS()
        self.assertTrue(
            gjtk.validate.hasBbox(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_valid_Feature_CRS(self):
        """ should return true when provided a Feature with a valid CRS """
        test_data = gjtk.random.Feature()
        test_data['crs'] = gjtk.random.CRS()
        self.assertTrue(
            gjtk.validate.hasBbox(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_valid_FeatureCollection_CRS(self):
        """ should return true when provided a FeatureCollection with a valid CRS """
        test_data = gjtk.random.FeatureCollection()
        test_data['crs'] = gjtk.random.CRS()
        self.assertTrue(
            gjtk.validate.hasBbox(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.hasCRS(test_data),
            gjtk.test.error_message(test_data)
        )



class isLinkTest (unittest.TestCase):

    def test_valid_Link(self):
        """ should return true when provided a valid Link object """
        test_data = gjtk.random.Link()
        self.assertTrue(
            gjtk.validate.isLink(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_no_type(self):
        """ should return true when provided a Link object without a type """
        test_data = gjtk.random.Link()
        if test_data.has_key('type'):
            del test_data['type']
        self.assertTrue(
            gjtk.validate.isLink(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_no_href(self):
        """ should return false when provided a Link object without href """
        test_data = gjtk.random.Link()
        del test_data['href']
        self.assertFalse(
            gjtk.validate.isLink(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.isLink(test_data),
            gjtk.test.error_message(test_data)
        )


class isBboxTest (unittest.TestCase):

    def test_valid_Bbox(self):
        """ should return true when provided a valid Bbox """
        test_data = gjtk.random.Bbox()
        self.assertTrue(
            gjtk.validate.isBbox(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            {},
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.isBbox(test_data),
            gjtk.test.error_message(test_data)
        )


class hasBboxTest (unittest.TestCase):

    def test_valid_Geometry_Bbox(self):
        """ should return true when provided a Geometry with a valid Bbox """
        test_data = gjtk.random.Geometry()
        test_data['bbox'] = gjtk.random.Bbox()
        self.assertTrue(
            gjtk.validate.hasBbox(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_valid_Feature_Bbox(self):
        """ should return true when provided a Feature with a valid Bbox """
        test_data = gjtk.random.Feature()
        test_data['bbox'] = gjtk.random.Bbox()
        self.assertTrue(
            gjtk.validate.hasBbox(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_valid_FeatureCollection_Bbox(self):
        """ should return true when provided a FeatureCollection with a valid Bbox """
        test_data = gjtk.random.FeatureCollection()
        test_data['bbox'] = gjtk.random.Bbox()
        self.assertTrue(
            gjtk.validate.hasBbox(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_invalid(self):
        """ should return false when provided an invalid object """
        test_data = random.choice([
            True,
            0,
            '',
            [],
            random.choice,
            None
        ])
        self.assertFalse(
            gjtk.validate.hasBbox(test_data),
            gjtk.test.error_message(test_data)
        )


##################################################################### COMPARISON


class equalPositions (unittest.TestCase):

    def test_same(self):
        """ should return true when provided identical Positions """
        test_data = gjtk.random.Position(max_numbers=6)
        self.assertTrue(
            gjtk.validate.equalPositions(test_data, test_data),
            gjtk.test.error_message(test_data)
        )

    def test_diff(self):
        """ should return false when provided different Positions """
        test_data1 = gjtk.random.Position(max_numbers=6)
        test_data2 = gjtk.random.Position(max_numbers=6)
        while test_data1[0] == test_data2[0]:
            gjtk.random.Position(max_numbers=6)
        self.assertFalse(
            gjtk.validate.equalPositions(test_data1, test_data2),
            gjtk.test.error_message([test_data1, test_data2])
        )


class containedPolygon (unittest.TestCase):

    def setUp(self):
        self.inner = [[1, 1], [1, 2], [2, 2], [2, 1], [1, 1]]
        self.outer = [[0, 0], [0, 5], [5, 5], [5, 0], [0, 0]]
    
    def test_contained(self):
        """ should return true when provided a LinearRing that contains another LinearRing. """
        self.assertTrue(gjtk.validate.containedPolygon(self.inner, self.outer))

    def test_not_contained(self):
        """ should return false when provided a LinearRing that does not contain another LinearRing. """
        self.assertFalse(gjtk.validate.containedPolygon(self.outer, self.inner))


if __name__ == "__main__":
    unittest.main()

