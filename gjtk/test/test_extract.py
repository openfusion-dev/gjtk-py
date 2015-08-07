

import unittest

import gjtk


class positionsOfTest (unittest.TestCase):

    def test_valid_Point(self):
        """ should return valid positions when provided a valid Point """
        test_data = gjtk.random.Point()
        test_result = gjtk.extract.positionsOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isPosition(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_valid_MultiPoint(self):
        """ should return valid positions when provided a valid MultiPoint """
        test_data = gjtk.random.MultiPoint()
        test_result = gjtk.extract.positionsOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isPosition(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_valid_LineString(self):
        """ should return valid positions when provided a valid LineString """
        test_data = gjtk.random.LineString()
        test_result = gjtk.extract.positionsOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isPosition(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_valid_MultiLineString(self):
        """ should return valid positions when provided a valid MultiLineString """
        test_data = gjtk.random.MultiLineString()
        test_result = gjtk.extract.positionsOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isPosition(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_valid_Polygon(self):
        """ should return valid positions when provided a valid Polygon """
        test_data = gjtk.random.Polygon()
        test_result = gjtk.extract.positionsOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isPosition(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_valid_MultiPolygon(self):
        """ should return valid positions when provided a valid MultiPolygon """
        test_data = gjtk.random.MultiPolygon()
        test_result = gjtk.extract.positionsOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isPosition(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_valid_GeometryCollection(self):
        """ should return valid positions when provided a valid GeometryCollection """
        test_data = gjtk.random.GeometryCollection()
        test_result = gjtk.extract.positionsOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isPosition(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_valid_Feature(self):
        """ should return valid positions when provided a valid Feature """
        test_data = gjtk.random.Feature()
        test_result = gjtk.extract.positionsOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isPosition(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_valid_FeatureCollection(self):
        """ should return valid positions when provided a valid FeatureCollection """
        test_data = gjtk.random.FeatureCollection()
        test_result = gjtk.extract.positionsOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isPosition(position) for position in test_result),
            gjtk.test.error_message(test_data, test_result)
        )


class featureOfTest (unittest.TestCase):

    def test_valid_Feature(self):
        """ should return valid features when provided a valid Feature """
        test_data = gjtk.random.Feature()
        test_result = gjtk.extract.featuresOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isFeature(feature) for feature in test_result),
            gjtk.test.error_message(test_data, test_result)
        )

    def test_valid_FeatureCollection(self):
        """ should return valid features when provided a valid FeatureCollection """
        test_data = gjtk.random.FeatureCollection()
        test_result = gjtk.extract.featuresOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isFeature(feature) for feature in test_result),
            gjtk.test.error_message(test_data, test_result)
        )


class geometriesOf (unittest.TestCase):

    def test_valid_Point(self):
        """ should return valid geometries when provided a valid Point """
        test_data = gjtk.random.Point()
        test_result = gjtk.extract.geometriesOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isGeometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result)
        )
    
    def test_valid_MultiPoint(self):
        """ should return valid geometries when provided a valid MultiPoint """
        test_data = gjtk.random.MultiPoint()
        test_result = gjtk.extract.geometriesOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isGeometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result)
        )
    
    def test_valid_LineString(self):
        """ should return valid geometries when provided a valid LineString """
        test_data = gjtk.random.LineString()
        test_result = gjtk.extract.geometriesOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isGeometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result)
        )
    
    def test_valid_MultiLineString(self):
        """ should return valid geometries when provided a valid MultiLineString """
        test_data = gjtk.random.MultiLineString()
        test_result = gjtk.extract.geometriesOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isGeometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result)
        )
    
    def test_valid_Polygon(self):
        """ should return valid geometries when provided a valid Polygon """
        test_data = gjtk.random.Polygon()
        test_result = gjtk.extract.geometriesOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isGeometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result)
        )
    
    def test_valid_MultiPolygon(self):
        """ should return valid geometries when provided a valid MultiPolygon """
        test_data = gjtk.random.MultiPolygon()
        test_result = gjtk.extract.geometriesOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isGeometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result)
        )
    
    def test_valid_GeometryCollection(self):
        """ should return valid geometries when provided a valid GeometryCollection """
        test_data = gjtk.random.GeometryCollection()
        test_result = gjtk.extract.geometriesOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isGeometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result)
        )
    
    def test_valid_Feature(self):
        """ should return valid geometries when provided a valid Feature """
        test_data = gjtk.random.Feature()
        test_result = gjtk.extract.geometriesOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isGeometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result)
        )
    
    def test_valid_FeatureCollection(self):
        """ should return valid geometries when provided a valid FeatureCollection """
        test_data = gjtk.random.FeatureCollection()
        test_result = gjtk.extract.geometriesOf(test_data)
        self.assertTrue(
            all(gjtk.validate.isGeometry(geometry) for geometry in test_result),
            gjtk.test.error_message(test_data, test_result)
        )


if __name__ == "__main__":
    unittest.main()

