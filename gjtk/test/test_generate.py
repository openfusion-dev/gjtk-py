

import random
import unittest

import gjtk


class TemplateTest (unittest.TestCase):

    def test_Point(self):
        """ should return a valid Point object when provided a valid Position """
        self.assertTrue(gjtk.validate.isPoint(gjtk.generate.Point(gjtk.generate.randomPosition())))

    def test_Feature(self):
        """ should return a valid Feature object when provided a valid Geometry """
        self.assertTrue(gjtk.validate.isFeature(gjtk.generate.Feature(gjtk.generate.randomGeometry())))

    def test_FeatureCollection(self):
        """ should return a valid FeatureCollection object when provided valid Features """
        length = round(random.random()*100)%3
        self.assertTrue(gjtk.validate.isFeatureCollection(gjtk.generate.FeatureCollection([gjtk.generate.randomFeature() for i in range(int(length))])))

    def test_FeatureCollection_empty(self):
        """ should return a valid FeatureCollection object when provided nothing """
        length = round(random.random()*100)%3
        self.assertTrue(gjtk.validate.isFeatureCollection(gjtk.generate.FeatureCollection()))

    def test_GeometryCollection(self):
        """ should return a valid GeometryCollection object when provided valid Geometries """
        length = round(random.random()*100)%3
        self.assertTrue(gjtk.validate.isGeometryCollection(gjtk.generate.GeometryCollection([gjtk.generate.randomGeometry() for i in range(int(length))])))

    def test_GeometryCollection_empty(self):
        """ should return a valid GeometryCollection object when provided nothing """
        length = round(random.random()*100)%3
        self.assertTrue(gjtk.validate.isGeometryCollection(gjtk.generate.GeometryCollection()))


class RandomTest (unittest.TestCase):

    def test_randomPosition(self):
        """ should return a valid Position """
        self.assertTrue(gjtk.validate.isPosition(gjtk.generate.randomPosition()))

    def test_randomPointCoordinates(self):
        """ should return a valid Point coordinates """
        self.assertTrue(gjtk.validate.isPointCoordinates(gjtk.generate.randomPointCoordinates()))

    def test_randomMultiPointCoordinates(self):
        """ should return a valid MultiPoint coordinates """
        self.assertTrue(gjtk.validate.isMultiPointCoordinates(gjtk.generate.randomMultiPointCoordinates()))

    def test_randomLineStringCoordinates(self):
        """ should return a valid LineString coordinates """
        self.assertTrue(gjtk.validate.isLineStringCoordinates(gjtk.generate.randomLineStringCoordinates()))

    def test_randomLinearRingCoordinates(self):
        """ should return a valid LinearRing coordinates """
        self.assertTrue(gjtk.validate.isLinearRingCoordinates(gjtk.generate.randomLinearRingCoordinates()))

    def test_randomMultiLineStringCoordinates(self):
        """ should return a valid MultiLineString coordinates """
        self.assertTrue(gjtk.validate.isMultiLineStringCoordinates(gjtk.generate.randomMultiLineStringCoordinates()))

    def test_randomPolygonCoordinates(self):
        """ should return a valid Polygon coordinates """
        self.assertTrue(gjtk.validate.isPolygonCoordinates(gjtk.generate.randomPolygonCoordinates()))

    def test_randomMultiPolygonCoordinates(self):
        """ should return a valid MultiPolygon coordinates """
        self.assertTrue(gjtk.validate.isMultiPolygonCoordinates(gjtk.generate.randomMultiPolygonCoordinates()))

    def test_randomGeometry(self):
        """ should return a valid Geometry """
        self.assertTrue(gjtk.validate.isGeometry(gjtk.generate.randomGeometry()))

    def test_randomMultiPoint(self):
        """ should return a valid MultiPoint """
        self.assertTrue(gjtk.validate.isMultiPoint(gjtk.generate.randomMultiPoint()))

    def test_randomLineString(self):
        """ should return a valid LineString """
        self.assertTrue(gjtk.validate.isLineString(gjtk.generate.randomLineString()))

    def test_randomMultiLineString(self):
        """ should return a valid MultiLineString """
        self.assertTrue(gjtk.validate.isMultiLineString(gjtk.generate.randomMultiLineString()))

    def test_randomPolygon(self):
        """ should return a valid Polygon """
        self.assertTrue(gjtk.validate.isPolygon(gjtk.generate.randomPolygon()))

    def test_randomMultiPolygon(self):
        """ should return a valid MultiPolygon """
        self.assertTrue(gjtk.validate.isMultiPolygon(gjtk.generate.randomMultiPolygon()))

    def test_randomGeometryCollection(self):
        """ should return a valid GeometryCollection """
        self.assertTrue(gjtk.validate.isGeometryCollection(gjtk.generate.randomGeometryCollection()))

    def test_randomGeometryCollection(self):
        """ should return a valid GeometryCollection """
        self.assertTrue(gjtk.validate.isGeometryCollection(gjtk.generate.randomGeometryCollection()))

    def test_randomFeature(self):
        """ should return a valid Feature """
        self.assertTrue(gjtk.validate.isFeature(gjtk.generate.randomFeature()))

    def test_randomFeatureCollection(self):
        """ should return a valid FeatureCollection """
        self.assertTrue(gjtk.validate.isFeatureCollection(gjtk.generate.randomFeatureCollection()))

    def test_randomCRS(self):
        """ should return a valid CRS """
        self.assertTrue(gjtk.validate.isCRS(gjtk.generate.randomCRS()))

    def test_randomLink(self):
        """ should return a valid Link """
        self.assertTrue(gjtk.validate.isLink(gjtk.generate.randomLink()))

    def test_randomBbox(self):
        """ should return a valid Bbox """
        self.assertTrue(gjtk.validate.isBbox(gjtk.generate.randomBbox()))


if __name__ == "__main__":
    unittest.main()

