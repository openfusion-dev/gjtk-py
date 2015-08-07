

import random
import unittest

import gjtk


class PointTest (unittest.TestCase):

    def test_valid_position(self):
        """ should return a valid Point object when provided a valid Position """
        test_data = gjtk.random.Position(max_numbers=6)
        test_result = gjtk.generate.Point(test_data)
        self.assertTrue(
            gjtk.validate.isPoint(test_result),
            gjtk.test.error_message(test_data, test_result)
        )


class MultiPointTest (unittest.TestCase):

    def test_valid_coordinates(self):
        """ should return a valid MultiPoint object when provided valid coordinates """
        test_data = gjtk.random.MultiPointCoordinates()
        test_result = gjtk.generate.MultiPoint(coordinates=test_data)
        self.assertTrue(
            gjtk.validate.isMultiPoint(test_result),
            gjtk.test.error_message(test_data, test_result)
        )


class LineStringTest (unittest.TestCase):

    def test_valid_coordinates(self):
        """ should return a valid LineString object when provided valid coordinates """
        test_data = gjtk.random.LineStringCoordinates()
        test_result = gjtk.generate.LineString(coordinates=test_data)
        self.assertTrue(
            gjtk.validate.isLineString(test_result),
            gjtk.test.error_message(test_data, test_result)
        )


class MultiLineStringTest (unittest.TestCase):

    def test_valid_coordinates(self):
        """ should return a valid MultiLineString object when provided valid coordinates """
        test_data = gjtk.random.MultiLineStringCoordinates()
        test_result = gjtk.generate.MultiLineString(coordinates=test_data)
        self.assertTrue(
            gjtk.validate.isMultiLineString(test_result),
            gjtk.test.error_message(test_data, test_result)
        )


class PolygonTest (unittest.TestCase):

    def test_valid_coordinates(self):
        """ should return a valid Polygon object when provided valid coordinates """
        test_data = gjtk.random.PolygonCoordinates()
        test_result = gjtk.generate.Polygon(coordinates=test_data)
        self.assertTrue(
            gjtk.validate.isPolygon(test_result),
            gjtk.test.error_message(test_data, test_result)
        )


class MultiPolygonTest (unittest.TestCase):

    def test_valid_coordinates(self):
        """ should return a valid MultiPolygon object when provided valid coordinates """
        test_data = gjtk.random.MultiPolygonCoordinates()
        test_result = gjtk.generate.MultiPolygon(coordinates=test_data)
        self.assertTrue(
            gjtk.validate.isMultiPolygon(test_result),
            gjtk.test.error_message(test_data, test_result)
        )


class GeometryCollectionTest (unittest.TestCase):

    def test_valid_geometries(self):
        """ should return a valid GeometryCollection object when provided valid Geometries """
        length = round(random.random()*100)%3
        test_data = [gjtk.random.Geometry() for i in range(int(length))]
        test_result = gjtk.generate.GeometryCollection(test_data)
        self.assertTrue(
            gjtk.validate.isGeometryCollection(test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_nothing(self):
        """ should return a valid GeometryCollection object when provided nothing """
        length = round(random.random()*100)%3
        test_data = None
        test_result = gjtk.generate.GeometryCollection(test_data)
        self.assertTrue(
            gjtk.validate.isGeometryCollection(test_result),
            gjtk.test.error_message(test_data, test_result)
        )


class FeatureTest (unittest.TestCase):

    def test_valid_geometry(self):
        """ should return a valid Feature object when provided a valid Geometry """
        test_data = gjtk.random.Geometry()
        test_result = gjtk.generate.Feature(test_data)
        self.assertTrue(
            gjtk.validate.isFeature(test_result),
            gjtk.test.error_message(test_data, test_result)
        )


class FeatureCollectionTest (unittest.TestCase):

    def test_valid_features(self):
        """ should return a valid FeatureCollection object when provided valid Features """
        length = round(random.random()*100)%3
        test_data = [gjtk.random.Feature() for i in range(int(length))]
        test_result = gjtk.generate.FeatureCollection(test_data)
        self.assertTrue(
            gjtk.validate.isFeatureCollection(test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_nothing(self):
        """ should return a valid FeatureCollection object when provided nothing """
        length = round(random.random()*100)%3
        test_data = None
        test_result = gjtk.generate.FeatureCollection(test_data)
        self.assertTrue(
            gjtk.validate.isFeatureCollection(test_result),
            gjtk.test.error_message(test_data, test_result)
        )


if __name__ == "__main__":
    unittest.main()

