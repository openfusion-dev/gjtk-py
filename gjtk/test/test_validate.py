

import copy
import unittest

import gjtk


class isGeoJSONTest (unittest.TestCase):

    def test_valid_Geometry(self):
        """ should return true when provided a valid Geometry object """
        self.assertTrue(gjtk.validate.isGeoJSON(gjtk.generate.randomGeometry()))

    def test_valid_Feature(self):
        """ should return true when provided a valid Feature object """
        self.assertTrue(gjtk.validate.isGeoJSON(gjtk.generate.randomFeature()))

    def test_valid_FeatureCollection(self):
        """ should return true when provided a valid Feature object """
        self.assertTrue(gjtk.validate.isGeoJSON(gjtk.generate.randomFeatureCollection()))


class isGeometryTest (unittest.TestCase):

    def test_valid_Point(self):
        """ should return true when provided a valid Point object """
        self.assertTrue(gjtk.validate.isGeometry(gjtk.generate.randomPoint()))

    def test_valid_MultiPoint(self):
        """ should return true when provided a valid MultiPoint object """
        self.assertTrue(gjtk.validate.isGeometry(gjtk.generate.randomMultiPoint()))

    def test_valid_LineString(self):
        """ should return true when provided a valid LineString object """
        self.assertTrue(gjtk.validate.isGeometry(gjtk.generate.randomLineString()))

    def test_valid_MultiLineString(self):
        """ should return true when provided a valid MultiLineString object """
        self.assertTrue(gjtk.validate.isGeometry(gjtk.generate.randomMultiLineString()))

    def test_valid_Polygon(self):
        """ should return true when provided a valid Polygon object """
        self.assertTrue(gjtk.validate.isGeometry(gjtk.generate.randomPolygon()))

    def test_valid_MultiPolygon(self):
        """ should return true when provided a valid MultiPolygon object """
        self.assertTrue(gjtk.validate.isGeometry(gjtk.generate.randomMultiPolygon()))

    def test_valid_GeometryCollection(self):
        """ should return true when provided a valid GeometryCollection object """
        self.assertTrue(gjtk.validate.isGeometry(gjtk.generate.randomGeometryCollection()))


class isPositionTest (unittest.TestCase):

    def test_valid_Position(self):
        """ should return true when provided an array of at least 2 numbers """
        self.assertTrue(gjtk.validate.isPosition(gjtk.generate.randomPosition()))

    def test_too_short(self):
        """ should return false when provided an array of less than 2 numbers """
        self.assertFalse(gjtk.validate.isPosition([1]))

    def test_incorrect_type(self):
        """ should return false when provided an array of at least 2 non-numbers """
        self.assertFalse(gjtk.validate.isPosition(['foo', 'bar']))

    def test_mixed_types(self):
        """ should return false when provided an array of a mix of at least 2 numbers and non-numbers """
        self.assertFalse(gjtk.validate.isPosition([1, 'a']))  # TODO Randomize ordering.

    def test_nothing(self):
        """ should return false when provided nothing """
        self.assertFalse(gjtk.validate.isPosition(None))


class isPointCoordinatesTest (unittest.TestCase):

    def test_valid_Point_coordinates(self):
        """ should return true when provided valid GeoJSON Point coordinates """
        self.assertTrue(gjtk.validate.isPointCoordinates(gjtk.generate.randomPointCoordinates()))


class isMultiPointCoordinatesTest (unittest.TestCase):

    def test_valid_MultiPoint_coordinates(self):
        """ should return true when provided valid GeoJSON MultiPoint coordinates """
        self.assertTrue(gjtk.validate.isMultiPointCoordinates(gjtk.generate.randomMultiPointCoordinates()))


class isLineStringCoordinatesTest (unittest.TestCase):

    def test_valid_LineString_coordinates(self):
        """ should return true when provided valid GeoJSON LineString coordinates """
        self.assertTrue(gjtk.validate.isLineStringCoordinates(gjtk.generate.randomLineStringCoordinates()))


class isLinearRingCoordinatesTest (unittest.TestCase):

    def test_valid_LinearRing_coordinates(self):
        """ should return true when provided a valid GeoJSON LinearRing """
        self.assertTrue(gjtk.validate.isLinearRingCoordinates(gjtk.generate.randomLinearRingCoordinates()))


class isMultiLineStringCoordinatesTest (unittest.TestCase):

    def test_valid_MultiLineString_coordinates(self):
        """ should return true when provided valid GeoJSON MultiLineString coordinates """
        self.assertTrue(gjtk.validate.isMultiLineStringCoordinates(gjtk.generate.randomMultiLineStringCoordinates()))


class isPolygonCoordinatesTest (unittest.TestCase):

    def test_valid_Polygon_coordinates(self):
        """ should return true when provided valid GeoJSON Polygon coordinates """
        self.assertTrue(gjtk.validate.isPolygonCoordinates(gjtk.generate.randomPolygonCoordinates()))


class isMultiPolygonCoordinatesTest (unittest.TestCase):

    def test_valid_MultiPolygon_coordinates(self):
        """ should return true when provided valid GeoJSON MultiPolygon coordinates """
        self.assertTrue(gjtk.validate.isMultiPolygonCoordinates(gjtk.generate.randomMultiPolygonCoordinates()))


class isPointTest (unittest.TestCase):

    def test_valid_Point(self):
        """ should return true when provided a valid Point object """
        self.assertTrue(gjtk.validate.isPoint(gjtk.generate.randomPoint()))

    def test_no_type(self):
        """ should return false when provided a Point object without a type """
        point = gjtk.generate.randomPoint()
        del point['type']
        self.assertFalse(gjtk.validate.isPoint(point))

    def test_no_coordinates(self):
        """ should return false when provided a Point object without coordinates """
        point = gjtk.generate.randomPoint()
        del point['coordinates']
        self.assertFalse(gjtk.validate.isPoint(point))

    def test_nothing(self):
        """ should return false when provided nothing """
        self.assertFalse(gjtk.validate.isPoint(None))


class isMultiPointTest (unittest.TestCase):

    def test_valid_MultiPoint(self):
        """ should return true when provided a valid MultiPoint object """
        self.assertTrue(gjtk.validate.isMultiPoint(gjtk.generate.randomMultiPoint()))

    def test_no_type(self):
        """ should return false when provided a MultiPoint object without a type """
        multi_point = gjtk.generate.randomMultiPoint()
        del multi_point['type']
        self.assertFalse(gjtk.validate.isMultiPoint(multi_point))

    def test_no_coordinates(self):
        """ should return false when provided a MultiPoint object without coordinates """
        multi_point = gjtk.generate.randomMultiPoint()
        del multi_point['coordinates']
        self.assertFalse(gjtk.validate.isMultiPoint(multi_point))

    def test_nothing(self):
        """ should return false when provided nothing """
        self.assertFalse(gjtk.validate.isMultiPoint(None))


class isLineStringTest (unittest.TestCase):

    def test_valid_LineString(self):
        """ should return true when provided a valid LineString object """
        self.assertTrue(gjtk.validate.isLineString(gjtk.generate.randomLineString()))

    def test_no_type(self):
        """ should return false when provided a LineString object without a type """
        line_string = gjtk.generate.randomLineString()
        del line_string['type']
        self.assertFalse(gjtk.validate.isLineString(line_string))

    def test_no_coordinates(self):
        """ should return false when provided a LineString object without coordinates """
        line_string = gjtk.generate.randomLineString()
        del line_string['coordinates']
        self.assertFalse(gjtk.validate.isLineString(line_string))

    def test_nothing(self):
        """ should return false when provided nothing """
        self.assertFalse(gjtk.validate.isLineString(None))


class isMultiLineStringTest (unittest.TestCase):

    def test_valid_MultiLineString(self):
        """ should return true when provided a valid MultiLineString object """
        self.assertTrue(gjtk.validate.isMultiLineString(gjtk.generate.randomMultiLineString()))

    def test_no_type(self):
        """ should return false when provided a MultiLineString object without a type """
        multi_line_string = gjtk.generate.randomMultiLineString()
        del multi_line_string['type']
        self.assertFalse(gjtk.validate.isMultiLineString(multi_line_string))

    def test_no_coordinates(self):
        """ should return false when provided a MultiLineString object without coordinates """
        multi_line_string = gjtk.generate.randomMultiLineString()
        del multi_line_string['coordinates']
        self.assertFalse(gjtk.validate.isMultiLineString(multi_line_string))

    def test_nothing(self):
        """ should return false when provided nothing """
        self.assertFalse(gjtk.validate.isMultiLineString(None))


class isPolygonTest (unittest.TestCase):

    def test_valid_Polygon(self):
        """ should return true when provided a valid Polygon object """
        self.assertTrue(gjtk.validate.isPolygon(gjtk.generate.randomPolygon()))

    def test_no_type(self):
        """ should return false when provided a Polygon object without a type """
        polygon = gjtk.generate.randomPolygon()
        del polygon['type']
        self.assertFalse(gjtk.validate.isPolygon(polygon))

    def test_no_coordinates(self):
        """ should return false when provided a Polygon object without coordinates """
        polygon = gjtk.generate.randomPolygon()
        del polygon['coordinates']
        self.assertFalse(gjtk.validate.isPolygon(polygon))

    def test_nothing(self):
        """ should return false when provided nothing """
        self.assertFalse(gjtk.validate.isPolygon(None))


class isMultiPolygonTest (unittest.TestCase):

    def test_valid_MultiPolygon(self):
        """ should return true when provided a valid MultiPolygon object """
        self.assertTrue(gjtk.validate.isMultiPolygon(gjtk.generate.randomMultiPolygon()))

    def test_no_type(self):
        """ should return false when provided a MultiPolygon object without a type """
        multi_polygon = gjtk.generate.randomMultiPolygon()
        del multi_polygon['type']
        self.assertFalse(gjtk.validate.isMultiPolygon(multi_polygon))

    def test_no_coordinates(self):
        """ should return false when provided a MultiPolygon object without coordinates """
        multi_polygon = gjtk.generate.randomMultiPolygon()
        del multi_polygon['coordinates']
        self.assertFalse(gjtk.validate.isMultiPolygon(multi_polygon))

    def test_nothing(self):
        """ should return false when provided nothing """
        self.assertFalse(gjtk.validate.isMultiPolygon(None))


class isGeometryCollectionTest (unittest.TestCase):

    def test_valid_GeometryCollection(self):
        """ should return true when provided a valid GeometryCollection object """
        self.assertTrue(gjtk.validate.isGeometryCollection(gjtk.generate.randomGeometryCollection()))

    def test_no_type(self):
        """ should return false when provided a GeometryCollection object without a type """
        geometry_collection = gjtk.generate.randomGeometryCollection()
        del geometry_collection['type']
        self.assertFalse(gjtk.validate.isGeometryCollection(geometry_collection))

    def test_no_geometries(self):
        """ should return false when provided a GeometryCollection object without geometries """
        geometry_collection = gjtk.generate.randomGeometryCollection()
        del geometry_collection['geometries']
        self.assertFalse(gjtk.validate.isGeometryCollection(geometry_collection))

    def test_nothing(self):
        """ should return false when provided nothing """
        self.assertFalse(gjtk.validate.isGeometryCollection(None))


class isFeatureTest (unittest.TestCase):

    def test_valid_Feature(self):
        """ should return true when provided a valid Feature object """
        self.assertTrue(gjtk.validate.isFeature(gjtk.generate.randomFeature()))

    def test_no_type(self):
        """ should return false when provided a Feature object without a type """
        feature = gjtk.generate.randomFeature()
        del feature['type']
        self.assertFalse(gjtk.validate.isFeature(feature))

    def test_no_geometry(self):
        """ should return false when provided a Feature object without geometry """
        feature = gjtk.generate.randomFeature()
        del feature['geometry']
        self.assertFalse(gjtk.validate.isFeature(feature))

    def test_nothing(self):
        """ should return false when provided nothing """
        self.assertFalse(gjtk.validate.isFeature(None))


class isFeatureCollectionTest (unittest.TestCase):

    def test_valid_FeatureCollection(self):
        """ should return true when provided a valid FeatureCollection object """
        self.assertTrue(gjtk.validate.isFeatureCollection(gjtk.generate.randomFeatureCollection()))

    def test_no_type(self):
        """ should return false when provided a FeatureCollection object without a type """
        feature_collection = gjtk.generate.randomFeatureCollection()
        del feature_collection['type']
        self.assertFalse(gjtk.validate.isFeatureCollection(feature_collection))

    def test_no_features(self):
        """ should return false when provided a FeatureCollection object without features """
        feature_collection = gjtk.generate.randomFeatureCollection()
        del feature_collection['features']
        self.assertFalse(gjtk.validate.isFeatureCollection(feature_collection))

    def test_nothing(self):
        """ should return false when provided nothing """
        self.assertFalse(gjtk.validate.isFeatureCollection(None))


class isCRSTest (unittest.TestCase):

    def test_(self):
        """ should return true when provided a valid CRS object """
        self.assertTrue(gjtk.validate.isCRS(gjtk.generate.randomCRS()))

    def test_(self):
        """ should return false when provided a CRS object without a type """
        crs = gjtk.generate.randomCRS()
        del crs['type']
        self.assertFalse(gjtk.validate.isCRS(crs))

    def test_(self):
        """ should return false when provided a CRS object without properties """
        crs = gjtk.generate.randomCRS()
        del crs['properties']
        self.assertFalse(gjtk.validate.isCRS(crs))

    def test_(self):
        """ should return false when provided nothing """
        self.assertFalse(gjtk.validate.isCRS(None))


class hasCRSTest (unittest.TestCase):

    def test_valid_Geometry_CRS(self):
        """ should return true when provided a Geometry with a valid CRS """
        geometry_CRS = gjtk.generate.randomGeometry()
        geometry_CRS['crs'] = gjtk.generate.randomCRS()
        self.assertTrue(gjtk.validate.hasBbox(geometry_CRS))

    def test_valid_Feature_CRS(self):
        """ should return true when provided a Feature with a valid CRS """
        feature_CRS = gjtk.generate.randomFeature()
        feature_CRS['crs'] = gjtk.generate.randomCRS()
        self.assertTrue(gjtk.validate.hasBbox(feature_CRS))

    def test_valid_FeatureCollection_CRS(self):
        """ should return true when provided a FeatureCollection with a valid CRS """
        feature_collection_CRS = gjtk.generate.randomFeatureCollection()
        feature_collection_CRS['crs'] = gjtk.generate.randomCRS()
        self.assertTrue(gjtk.validate.hasBbox(feature_collection_CRS))



class isLinkTest (unittest.TestCase):

    def test_valid_Link(self):
        """ should return true when provided a valid Link object """
        self.assertTrue(gjtk.validate.isLink(gjtk.generate.randomLink()))

    def test_no_type(self):
        """ should return true when provided a Link object without a type """
        link = gjtk.generate.randomLink()
        del link['type']
        self.assertTrue(gjtk.validate.isLink(link))

    def test_no_href(self):
        """ should return false when provided a Link object without href """
        link = gjtk.generate.randomLink()
        del link['href']
        self.assertFalse(gjtk.validate.isLink(link))

    def test_nothing(self):
        """ should return false when provided nothing """
        self.assertFalse(gjtk.validate.isLink(None))


class isBboxTest (unittest.TestCase):

    def test_valid_Bbox(self):
        """ should return true when provided a valid Bbox """
        self.assertTrue(gjtk.validate.isBbox(gjtk.generate.randomBbox()))


class hasBboxTest (unittest.TestCase):

    def test_valid_Geometry_Bbox(self):
        """ should return true when provided a Geometry with a valid Bbox """
        geometry_bbox = gjtk.generate.randomGeometry()
        geometry_bbox['bbox'] = gjtk.generate.randomBbox()
        self.assertTrue(gjtk.validate.hasBbox(geometry_bbox))

    def test_valid_Feature_Bbox(self):
        """ should return true when provided a Feature with a valid Bbox """
        feature_bbox = gjtk.generate.randomFeature()
        feature_bbox['bbox'] = gjtk.generate.randomBbox()
        self.assertTrue(gjtk.validate.hasBbox(feature_bbox))

    def test_valid_FeatureCollection_Bbox(self):
        """ should return true when provided a FeatureCollection with a valid Bbox """
        feature_collection_bbox = gjtk.generate.randomFeatureCollection()
        feature_collection_bbox['bbox'] = gjtk.generate.randomBbox()
        self.assertTrue(gjtk.validate.hasBbox(feature_collection_bbox))


##################################################################### COMPARISON


class equalPositions (unittest.TestCase):

    def test_same(self):
        """ should return true when provided identical Positions """
        position = gjtk.generate.randomPosition()
        self.assertTrue(gjtk.validate.equalPositions(position, position))

    def test_diff(self):
        """ should return false when provided different Positions """
        positionA = gjtk.generate.randomPosition()
        positionB = copy.deepcopy(positionA)
        positionB[0] += 1
        self.assertFalse(gjtk.validate.equalPositions(positionA, positionB))


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

