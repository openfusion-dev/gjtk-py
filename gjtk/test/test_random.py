

import unittest

import gjtk


class RandomTest (unittest.TestCase):

    def test_randomPosition(self):
        """ should return a valid Position """
        test_data = gjtk.random.Position(max_numbers=6)
        self.assertTrue(
            gjtk.validate.isPosition(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomPointCoordinates(self):
        """ should return a valid Point coordinates """
        test_data = gjtk.random.PointCoordinates()
        self.assertTrue(
            gjtk.validate.isPointCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomMultiPointCoordinates(self):
        """ should return a valid MultiPoint coordinates """
        test_data = gjtk.random.MultiPointCoordinates()
        self.assertTrue(
            gjtk.validate.isMultiPointCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomLineStringCoordinates(self):
        """ should return a valid LineString coordinates """
        test_data = gjtk.random.LineStringCoordinates()
        self.assertTrue(
            gjtk.validate.isLineStringCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomLinearRingCoordinates(self):
        """ should return a valid LinearRing coordinates """
        test_data = gjtk.random.LinearRingCoordinates()
        self.assertTrue(
            gjtk.validate.isLinearRingCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomMultiLineStringCoordinates(self):
        """ should return a valid MultiLineString coordinates """
        test_data = gjtk.random.MultiLineStringCoordinates()
        self.assertTrue(
            gjtk.validate.isMultiLineStringCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomPolygonCoordinates(self):
        """ should return a valid Polygon coordinates """
        test_data = gjtk.random.PolygonCoordinates()
        self.assertTrue(
            gjtk.validate.isPolygonCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomMultiPolygonCoordinates(self):
        """ should return a valid MultiPolygon coordinates """
        test_data = gjtk.random.MultiPolygonCoordinates()
        self.assertTrue(
            gjtk.validate.isMultiPolygonCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomGeometry(self):
        """ should return a valid Geometry """
        test_data = gjtk.random.Geometry()
        self.assertTrue(
            gjtk.validate.isGeometry(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomMultiPoint(self):
        """ should return a valid MultiPoint """
        test_data = gjtk.random.MultiPoint()
        self.assertTrue(
            gjtk.validate.isMultiPoint(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomLineString(self):
        """ should return a valid LineString """
        test_data = gjtk.random.LineString()
        self.assertTrue(
            gjtk.validate.isLineString(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomMultiLineString(self):
        """ should return a valid MultiLineString """
        test_data = gjtk.random.MultiLineString()
        self.assertTrue(
            gjtk.validate.isMultiLineString(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomPolygon(self):
        """ should return a valid Polygon """
        test_data = gjtk.random.Polygon()
        self.assertTrue(
            gjtk.validate.isPolygon(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomMultiPolygon(self):
        """ should return a valid MultiPolygon """
        test_data = gjtk.random.MultiPolygon()
        self.assertTrue(
            gjtk.validate.isMultiPolygon(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomGeometryCollection(self):
        """ should return a valid GeometryCollection """
        test_data = gjtk.random.GeometryCollection()
        self.assertTrue(
            gjtk.validate.isGeometryCollection(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomGeometryCollection(self):
        """ should return a valid GeometryCollection """
        test_data = gjtk.random.GeometryCollection()
        self.assertTrue(
            gjtk.validate.isGeometryCollection(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomFeature(self):
        """ should return a valid Feature """
        test_data = gjtk.random.Feature()
        self.assertTrue(
            gjtk.validate.isFeature(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomFeatureCollection(self):
        """ should return a valid FeatureCollection """
        test_data = gjtk.random.FeatureCollection()
        self.assertTrue(
            gjtk.validate.isFeatureCollection(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomCRS(self):
        """ should return a valid CRS """
        test_data = gjtk.random.CRS()
        self.assertTrue(
            gjtk.validate.isCRS(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomLink(self):
        """ should return a valid Link """
        test_data = gjtk.random.Link()
        self.assertTrue(
            gjtk.validate.isLink(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomBbox(self):
        """ should return a valid Bbox """
        test_data = gjtk.random.Bbox()
        self.assertTrue(
            gjtk.validate.isBbox(test_data),
            gjtk.test.error_message(test_data)
        )


if __name__ == "__main__":
    unittest.main()

