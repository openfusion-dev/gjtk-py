

import unittest

import gjtk


class PositionTest (unittest.TestCase):

    def test_valid_Position(self):
        """ should return a valid Position """
        test_data = gjtk.random.Position(max_numbers=6)
        self.assertTrue(
            gjtk.validate.isPosition(test_data),
            gjtk.test.error_message(test_data)
        )


class PointCoordinatesTest (unittest.TestCase):

    def test_valid_PointCoordinates(self):
        """ should return a valid Point coordinates """
        test_data = gjtk.random.PointCoordinates()
        self.assertTrue(
            gjtk.validate.isPointCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )


class MultiPointCoordinatesTest (unittest.TestCase):

    def test_valid_MultiPointCoordinates(self):
        """ should return a valid MultiPoint coordinates """
        test_data = gjtk.random.MultiPointCoordinates()
        self.assertTrue(
            gjtk.validate.isMultiPointCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )


class LineStringCoordinatesTest (unittest.TestCase):

    def test_valid_LineStringCoordinates(self):
        """ should return a valid LineString coordinates """
        test_data = gjtk.random.LineStringCoordinates()
        self.assertTrue(
            gjtk.validate.isLineStringCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )


class LinearRingCoordinatesTest (unittest.TestCase):

    def test_valid_LinearRingCoordinates(self):
        """ should return a valid LinearRing coordinates """
        test_data = gjtk.random.LinearRingCoordinates()
        self.assertTrue(
            gjtk.validate.isLinearRingCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )


class MultiLineStringCoordinatesTest (unittest.TestCase):

    def test_valid_MultiLineStringCoordinates(self):
        """ should return a valid MultiLineString coordinates """
        test_data = gjtk.random.MultiLineStringCoordinates()
        self.assertTrue(
            gjtk.validate.isMultiLineStringCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )


class PolygonCoordinatesTest (unittest.TestCase):

    def test_valid_PolygonCoordinates(self):
        """ should return a valid Polygon coordinates """
        test_data = gjtk.random.PolygonCoordinates()
        self.assertTrue(
            gjtk.validate.isPolygonCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )


class MultiPolygonCoordinatesTest (unittest.TestCase):

    def test_valid_MultiPolygonCoordinates(self):
        """ should return a valid MultiPolygon coordinates """
        test_data = gjtk.random.MultiPolygonCoordinates()
        self.assertTrue(
            gjtk.validate.isMultiPolygonCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )


class GeometryTest (unittest.TestCase):

    def test_valid_Geometry(self):
        """ should return a valid Geometry """
        test_data = gjtk.random.Geometry()
        self.assertTrue(
            gjtk.validate.isGeometry(test_data),
            gjtk.test.error_message(test_data)
        )


class PointTest (unittest.TestCase):

    def test_valid_Point(self):
        """ should return a valid Point """
        test_data = gjtk.random.Point()
        self.assertTrue(
            gjtk.validate.isPoint(test_data),
            gjtk.test.error_message(test_data)
        )


class MultiPointTest (unittest.TestCase):

    def test_valid_MultiPoint(self):
        """ should return a valid MultiPoint """
        test_data = gjtk.random.MultiPoint()
        self.assertTrue(
            gjtk.validate.isMultiPoint(test_data),
            gjtk.test.error_message(test_data)
        )


class LineStringTest (unittest.TestCase):

    def test_valid_LineString(self):
        """ should return a valid LineString """
        test_data = gjtk.random.LineString()
        self.assertTrue(
            gjtk.validate.isLineString(test_data),
            gjtk.test.error_message(test_data)
        )


class MultiLineStringTest (unittest.TestCase):

    def test_valid_MultiLineString(self):
        """ should return a valid MultiLineString """
        test_data = gjtk.random.MultiLineString()
        self.assertTrue(
            gjtk.validate.isMultiLineString(test_data),
            gjtk.test.error_message(test_data)
        )


class PolygonTest (unittest.TestCase):

    def test_valid_Polygon(self):
        """ should return a valid Polygon """
        test_data = gjtk.random.Polygon()
        self.assertTrue(
            gjtk.validate.isPolygon(test_data),
            gjtk.test.error_message(test_data)
        )


class MultiPolygonTest (unittest.TestCase):

    def test_valid_MultiPolygon(self):
        """ should return a valid MultiPolygon """
        test_data = gjtk.random.MultiPolygon()
        self.assertTrue(
            gjtk.validate.isMultiPolygon(test_data),
            gjtk.test.error_message(test_data)
        )


class GeometryCollectionTest (unittest.TestCase):

    def test_valid_GeometryCollection(self):
        """ should return a valid GeometryCollection """
        test_data = gjtk.random.GeometryCollection()
        self.assertTrue(
            gjtk.validate.isGeometryCollection(test_data),
            gjtk.test.error_message(test_data)
        )


class FeatureTest (unittest.TestCase):

    def test_valid_Feature(self):
        """ should return a valid Feature """
        test_data = gjtk.random.Feature()
        self.assertTrue(
            gjtk.validate.isFeature(test_data),
            gjtk.test.error_message(test_data)
        )


class FeatureCollectionTest (unittest.TestCase):

    def test_valid_FeatureCollection(self):
        """ should return a valid FeatureCollection """
        test_data = gjtk.random.FeatureCollection()
        self.assertTrue(
            gjtk.validate.isFeatureCollection(test_data),
            gjtk.test.error_message(test_data)
        )


class CRSTest (unittest.TestCase):

    def test_valid_CRS(self):
        """ should return a valid CRS """
        test_data = gjtk.random.CRS()
        self.assertTrue(
            gjtk.validate.isCRS(test_data),
            gjtk.test.error_message(test_data)
        )


class LinkTest (unittest.TestCase):

    def test_valid_Link(self):
        """ should return a valid Link """
        test_data = gjtk.random.Link()
        self.assertTrue(
            gjtk.validate.isLink(test_data),
            gjtk.test.error_message(test_data)
        )


class BboxTest (unittest.TestCase):

    def test_valid_Bbox(self):
        """ should return a valid Bbox """
        test_data = gjtk.random.Bbox()
        self.assertTrue(
            gjtk.validate.isBbox(test_data),
            gjtk.test.error_message(test_data)
        )


if __name__ == "__main__":
    unittest.main()

