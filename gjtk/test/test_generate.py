

import random
import unittest

import gjtk


class TemplateTest (unittest.TestCase):

    def test_Point(self):
        """ should return a valid Point object when provided a valid Position """
        test_data = gjtk.generate.randomPosition()
        test_result = gjtk.generate.Point(test_data)
        self.assertTrue(
            gjtk.validate.isPoint(test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_Feature(self):
        """ should return a valid Feature object when provided a valid Geometry """
        test_data = gjtk.generate.randomGeometry()
        test_result = gjtk.generate.Feature(test_data)
        self.assertTrue(
            gjtk.validate.isFeature(test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_FeatureCollection(self):
        """ should return a valid FeatureCollection object when provided valid Features """
        length = round(random.random()*100)%3
        test_data = [gjtk.generate.randomFeature() for i in range(int(length))]
        test_result = gjtk.generate.FeatureCollection(test_data)
        self.assertTrue(
            gjtk.validate.isFeatureCollection(test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_FeatureCollection_empty(self):
        """ should return a valid FeatureCollection object when provided nothing """
        length = round(random.random()*100)%3
        test_data = None
        test_result = gjtk.generate.FeatureCollection(test_data)
        self.assertTrue(
            gjtk.validate.isFeatureCollection(test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_GeometryCollection(self):
        """ should return a valid GeometryCollection object when provided valid Geometries """
        length = round(random.random()*100)%3
        test_data = [gjtk.generate.randomGeometry() for i in range(int(length))]
        test_result = gjtk.generate.GeometryCollection(test_data)
        self.assertTrue(
            gjtk.validate.isGeometryCollection(test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_GeometryCollection_empty(self):
        """ should return a valid GeometryCollection object when provided nothing """
        length = round(random.random()*100)%3
        test_data = None
        test_result = gjtk.generate.GeometryCollection(test_data)
        self.assertTrue(
            gjtk.validate.isGeometryCollection(test_result),
            gjtk.test.error_message(test_data, test_result)
        )


class RandomTest (unittest.TestCase):

    def test_randomPosition(self):
        """ should return a valid Position """
        test_data = gjtk.generate.randomPosition()
        self.assertTrue(
            gjtk.validate.isPosition(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomPointCoordinates(self):
        """ should return a valid Point coordinates """
        test_data = gjtk.generate.randomPointCoordinates()
        self.assertTrue(
            gjtk.validate.isPointCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomMultiPointCoordinates(self):
        """ should return a valid MultiPoint coordinates """
        test_data = gjtk.generate.randomMultiPointCoordinates()
        self.assertTrue(
            gjtk.validate.isMultiPointCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomLineStringCoordinates(self):
        """ should return a valid LineString coordinates """
        test_data = gjtk.generate.randomLineStringCoordinates()
        self.assertTrue(
            gjtk.validate.isLineStringCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomLinearRingCoordinates(self):
        """ should return a valid LinearRing coordinates """
        test_data = gjtk.generate.randomLinearRingCoordinates()
        self.assertTrue(
            gjtk.validate.isLinearRingCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomMultiLineStringCoordinates(self):
        """ should return a valid MultiLineString coordinates """
        test_data = gjtk.generate.randomMultiLineStringCoordinates()
        self.assertTrue(
            gjtk.validate.isMultiLineStringCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomPolygonCoordinates(self):
        """ should return a valid Polygon coordinates """
        test_data = gjtk.generate.randomPolygonCoordinates()
        self.assertTrue(
            gjtk.validate.isPolygonCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomMultiPolygonCoordinates(self):
        """ should return a valid MultiPolygon coordinates """
        test_data = gjtk.generate.randomMultiPolygonCoordinates()
        self.assertTrue(
            gjtk.validate.isMultiPolygonCoordinates(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomGeometry(self):
        """ should return a valid Geometry """
        test_data = gjtk.generate.randomGeometry()
        self.assertTrue(
            gjtk.validate.isGeometry(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomMultiPoint(self):
        """ should return a valid MultiPoint """
        test_data = gjtk.generate.randomMultiPoint()
        self.assertTrue(
            gjtk.validate.isMultiPoint(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomLineString(self):
        """ should return a valid LineString """
        test_data = gjtk.generate.randomLineString()
        self.assertTrue(
            gjtk.validate.isLineString(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomMultiLineString(self):
        """ should return a valid MultiLineString """
        test_data = gjtk.generate.randomMultiLineString()
        self.assertTrue(
            gjtk.validate.isMultiLineString(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomPolygon(self):
        """ should return a valid Polygon """
        test_data = gjtk.generate.randomPolygon()
        self.assertTrue(
            gjtk.validate.isPolygon(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomMultiPolygon(self):
        """ should return a valid MultiPolygon """
        test_data = gjtk.generate.randomMultiPolygon()
        self.assertTrue(
            gjtk.validate.isMultiPolygon(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomGeometryCollection(self):
        """ should return a valid GeometryCollection """
        test_data = gjtk.generate.randomGeometryCollection()
        self.assertTrue(
            gjtk.validate.isGeometryCollection(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomGeometryCollection(self):
        """ should return a valid GeometryCollection """
        test_data = gjtk.generate.randomGeometryCollection()
        self.assertTrue(
            gjtk.validate.isGeometryCollection(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomFeature(self):
        """ should return a valid Feature """
        test_data = gjtk.generate.randomFeature()
        self.assertTrue(
            gjtk.validate.isFeature(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomFeatureCollection(self):
        """ should return a valid FeatureCollection """
        test_data = gjtk.generate.randomFeatureCollection()
        self.assertTrue(
            gjtk.validate.isFeatureCollection(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomCRS(self):
        """ should return a valid CRS """
        test_data = gjtk.generate.randomCRS()
        self.assertTrue(
            gjtk.validate.isCRS(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomLink(self):
        """ should return a valid Link """
        test_data = gjtk.generate.randomLink()
        self.assertTrue(
            gjtk.validate.isLink(test_data),
            gjtk.test.error_message(test_data)
        )

    def test_randomBbox(self):
        """ should return a valid Bbox """
        test_data = gjtk.generate.randomBbox()
        self.assertTrue(
            gjtk.validate.isBbox(test_data),
            gjtk.test.error_message(test_data)
        )


if __name__ == "__main__":
    unittest.main()

