

import unittest

import gjtk


class positionsOfTest (unittest.TestCase):

    def test_valid_Point(self):
        """ should return valid positions when provided a valid Point """
        test_data = gjtk.generate.randomPoint()
        test_result = gjtk.extract.positionsOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isPosition(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_valid_MultiPoint(self):
        """ should return valid positions when provided a valid MultiPoint """
        test_data = gjtk.generate.randomMultiPoint()
        test_result = gjtk.extract.positionsOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isPosition(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_valid_LineString(self):
        """ should return valid positions when provided a valid LineString """
        test_data = gjtk.generate.randomLineString()
        test_result = gjtk.extract.positionsOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isPosition(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_valid_MultiLineString(self):
        """ should return valid positions when provided a valid MultiLineString """
        test_data = gjtk.generate.randomMultiLineString()
        test_result = gjtk.extract.positionsOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isPosition(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_valid_Polygon(self):
        """ should return valid positions when provided a valid Polygon """
        test_data = gjtk.generate.randomPolygon()
        test_result = gjtk.extract.positionsOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isPosition(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_valid_MultiPolygon(self):
        """ should return valid positions when provided a valid MultiPolygon """
        test_data = gjtk.generate.randomMultiPolygon()
        test_result = gjtk.extract.positionsOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isPosition(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_valid_GeometryCollection(self):
        """ should return valid positions when provided a valid GeometryCollection """
        test_data = gjtk.generate.randomGeometryCollection()
        test_result = gjtk.extract.positionsOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isPosition(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_valid_Feature(self):
        """ should return valid positions when provided a valid Feature """
        test_data = gjtk.generate.randomFeature()
        test_result = gjtk.extract.positionsOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isPosition(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_valid_FeatureCollection(self):
        """ should return valid positions when provided a valid FeatureCollection """
        test_data = gjtk.generate.randomFeatureCollection()
        test_result = gjtk.extract.positionsOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isPosition(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result)
        )


class featureOfTest (unittest.TestCase):

    def test_valid_Feature(self):
        """ should return valid features when provided a valid Feature """
        test_data = gjtk.generate.randomFeature()
        test_result = gjtk.extract.featuresOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isFeature(feature) for feature in test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_valid_FeatureCollection(self):
        """ should return valid features when provided a valid FeatureCollection """
        test_data = gjtk.generate.randomFeatureCollection()
        test_result = gjtk.extract.featuresOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isFeature(feature) for feature in test_result),
            gjtk.test.error_message(test_data, test_result)
        )


class geometriesOf (unittest.TestCase):

    def test_valid_Point(self):
        """ should return valid geometries when provided a valid Point """
        test_data = gjtk.generate.randomPoint()
        test_result = gjtk.extract.geometriesOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isGeometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result)
        )
    
    def test_valid_MultiPoint(self):
        """ should return valid geometries when provided a valid MultiPoint """
        test_data = gjtk.generate.randomMultiPoint()
        test_result = gjtk.extract.geometriesOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isGeometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result)
        )
    
    def test_valid_LineString(self):
        """ should return valid geometries when provided a valid LineString """
        test_data = gjtk.generate.randomLineString()
        test_result = gjtk.extract.geometriesOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isGeometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result)
        )
    
    def test_valid_MultiLineString(self):
        """ should return valid geometries when provided a valid MultiLineString """
        test_data = gjtk.generate.randomMultiLineString()
        test_result = gjtk.extract.geometriesOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isGeometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result)
        )
    
    def test_valid_Polygon(self):
        """ should return valid geometries when provided a valid Polygon """
        test_data = gjtk.generate.randomPolygon()
        test_result = gjtk.extract.geometriesOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isGeometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result)
        )
    
    def test_valid_MultiPolygon(self):
        """ should return valid geometries when provided a valid MultiPolygon """
        test_data = gjtk.generate.randomMultiPolygon()
        test_result = gjtk.extract.geometriesOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isGeometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result)
        )
    
    def test_valid_GeometryCollection(self):
        """ should return valid geometries when provided a valid GeometryCollection """
        test_data = gjtk.generate.randomGeometryCollection()
        test_result = gjtk.extract.geometriesOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isGeometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result)
        )
    
    def test_valid_Feature(self):
        """ should return valid geometries when provided a valid Feature """
        test_data = gjtk.generate.randomFeature()
        test_result = gjtk.extract.geometriesOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isGeometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result)
        )
    
    def test_valid_FeatureCollection(self):
        """ should return valid geometries when provided a valid FeatureCollection """
        test_data = gjtk.generate.randomFeatureCollection()
        test_result = gjtk.extract.geometriesOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isGeometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result)
        )


if __name__ == "__main__":
    unittest.main()

