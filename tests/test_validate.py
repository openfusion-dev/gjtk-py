"""Tests for gjtk.validate"""

import gjtk.validate


def test_is_geojson(geojson):
    """should return true when provided a valid GeoJSON object"""
    assert gjtk.validate.is_geojson(geojson)


def test_is_geojson_invalid(types):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.is_geojson(types)


def test_is_geometry(geometry):
    """should return true when provided a valid Geometry object"""
    assert gjtk.validate.is_geometry(geometry)


def test_is_geometry_invalid(types):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.is_geometry(types)


def test_is_position(position):
    """should return true when provided an array of at least 2 numbers"""
    assert gjtk.validate.is_position(position)


def test_is_position_invalid(invalid_position):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.is_position(invalid_position)


def test_is_point_coordinates(point_coordinates):
    """should return true when provided valid GeoJSON Point coordinates"""
    assert gjtk.validate.is_point_coordinates(point_coordinates)


def test_is_point_coordinates_invalid(types):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.is_point_coordinates(types)


def test_is_multi_point_coordinates(multi_point_coordinates):
    """should return true when provided valid GeoJSON MultiPoint coordinates"""
    assert gjtk.validate.is_multi_point_coordinates(multi_point_coordinates)


def test_is_multi_point_coordinates_invalid(immutable):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.is_multi_point_coordinates(immutable)


def test_is_line_string_coordinates(line_string_coordinates):
    """should return true when provided valid GeoJSON LineString coordinates"""
    assert gjtk.validate.is_line_string_coordinates(line_string_coordinates)


def test_is_line_string_coordinates_invalid(types):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.is_line_string_coordinates(types)


def test_is_linear_ring_coordinates(linear_ring_coordinates):
    """should return true when provided a valid GeoJSON LinearRing"""
    assert gjtk.validate.is_linear_ring_coordinates(linear_ring_coordinates)


def test_is_linear_ring_coordinates_invalid(types):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.is_linear_ring_coordinates(types)


def test_is_multi_line_string_coordinates(multi_line_string_coordinates):
    """should return true when provided valid GeoJSON MultiLineString coordinates"""
    assert gjtk.validate.is_multi_line_string_coordinates(multi_line_string_coordinates)


def test_is_multi_line_string_coordinates_invalid(immutable):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.is_multi_line_string_coordinates(immutable)


def test_is_polygon_coordinates(polygon_coordinates):
    """should return true when provided valid GeoJSON Polygon coordinates"""
    assert gjtk.validate.is_polygon_coordinates(polygon_coordinates)


def test_is_polygon_coordinates_invalid(immutable):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.is_polygon_coordinates(immutable)


def test_is_multi_polygon_coordinates(multi_polygon_coordinates):
    """should return true when provided valid GeoJSON MultiPolygon coordinates"""
    assert gjtk.validate.is_multi_polygon_coordinates(multi_polygon_coordinates)


def test_is_multi_polygon_coordinates_invalid(immutable):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.is_multi_polygon_coordinates(immutable)


def test_is_point(point):
    """should return true when provided a valid Point object"""
    assert gjtk.validate.is_point(point)


def test_is_point_no_type(point_without_type):
    """should return false when provided a Point object without a type"""
    assert not gjtk.validate.is_point(point_without_type)


def test_is_point_no_coordinates(point_without_coordinates):
    """should return false when provided a Point object without coordinates"""
    assert not gjtk.validate.is_point(point_without_coordinates)


def test_is_point_invalid(types):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.is_point(types)


def test_is_multi_point(multi_point):
    """should return true when provided a valid MultiPoint object"""
    assert gjtk.validate.is_multi_point(multi_point)


def test_is_multi_point_no_type(multi_point_without_type):
    """should return false when provided a MultiPoint object without a type"""
    assert not gjtk.validate.is_multi_point(multi_point_without_type)


def test_is_multi_point_no_coordinates(multi_point_without_coordinates):
    """should return false when provided a MultiPoint object without coordinates"""
    assert not gjtk.validate.is_multi_point(multi_point_without_coordinates)


def test_is_multi_point_invalid(types):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.is_multi_point(types)


def test_is_line_string(line_string):
    """should return true when provided a valid LineString object"""
    assert gjtk.validate.is_line_string(line_string)


def test_is_line_string_no_type(line_string_without_type):
    """should return false when provided a LineString object without a type"""
    assert not gjtk.validate.is_line_string(line_string_without_type)


def test_is_line_string_no_coordinates(line_string_without_coordinates):
    """should return false when provided a LineString object without coordinates"""
    assert not gjtk.validate.is_line_string(line_string_without_coordinates)


def test_is_line_string_invalid(types):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.is_line_string(types)


def test_is_multi_line_string(multi_line_string):
    """should return true when provided a valid MultiLineString object"""
    assert gjtk.validate.is_multi_line_string(multi_line_string)


def test_is_multi_line_string_no_type(multi_line_string_without_type):
    """should return false when provided a MultiLineString object without a type"""
    assert not gjtk.validate.is_multi_line_string(multi_line_string_without_type)


def test_is_multi_line_string_no_coordinates(multi_line_string_without_coordinates):
    """should return false when provided a MultiLineString object without coordinates"""
    assert not gjtk.validate.is_multi_line_string(multi_line_string_without_coordinates)


def test_is_multi_line_string_invalid(types):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.is_multi_line_string(types)


def test_is_polygon(polygon):
    """should return true when provided a valid Polygon object"""
    assert gjtk.validate.is_polygon(polygon)


def test_is_polygon_malformed(malformed_polygon):
    """should return false when provided a malformed Polygon"""
    assert not gjtk.validate.is_polygon(malformed_polygon)


def test_is_polygon_no_type(polygon_without_type):
    """should return false when provided a Polygon object without a type"""
    assert not gjtk.validate.is_polygon(polygon_without_type)


def test_is_polygon_no_coordinates(polygon_without_coordinates):
    """should return false when provided a Polygon object without coordinates"""
    assert not gjtk.validate.is_polygon(polygon_without_coordinates)


def test_is_polygon_invalid(types):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.is_polygon(types)


def test_is_multi_polygon(multi_polygon):
    """should return true when provided a valid MultiPolygon object"""
    assert gjtk.validate.is_multi_polygon(multi_polygon)


def test_is_multi_polygon_malformed(malformed_multi_polygon):
    """should return false when provided a malformed MultiPolygon"""
    assert not gjtk.validate.is_multi_polygon(malformed_multi_polygon)


def test_is_multi_polygon_no_type(multi_polygon_without_type):
    """should return false when provided a MultiPolygon object without a type"""
    assert not gjtk.validate.is_multi_polygon(multi_polygon_without_type)


def test_is_multi_polygon_no_coordinates(multi_polygon_without_coordinates):
    """should return false when provided a MultiPolygon object without coordinates"""
    assert not gjtk.validate.is_multi_polygon(multi_polygon_without_coordinates)


def test_is_multi_polygon_invalid(types):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.is_multi_polygon(types)


def test_is_geometry_collection(geometry_collection):
    """should return true when provided a valid GeometryCollection object"""
    assert gjtk.validate.is_geometry_collection(geometry_collection)


def test_is_geometry_collection_no_type(geometry_collection_without_type):
    """should return false when provided a GeometryCollection object without a type"""
    assert not gjtk.validate.is_geometry_collection(geometry_collection_without_type)


def test_is_geometry_collection_no_geometries(geometry_collection_without_geometries):
    """should return false when provided a GeometryCollection object without geometries"""
    assert not gjtk.validate.is_geometry_collection(geometry_collection_without_geometries)


def test_is_geometry_collection_invalid(types):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.is_geometry_collection(types)


def test_is_feature(feature):
    """should return true when provided a valid Feature object"""
    assert gjtk.validate.is_feature(feature)


def test_is_feature_no_type(feature_without_type):
    """should return false when provided a Feature object without a type"""
    assert not gjtk.validate.is_feature(feature_without_type)


def test_is_feature_no_geometry(feature_without_geometry):
    """should return false when provided a Feature object without geometry"""
    assert not gjtk.validate.is_feature(feature_without_geometry)


def test_is_feature_invalid(types):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.is_feature(types)


def test_is_feature_collection(feature_collection):
    """should return true when provided a valid FeatureCollection object"""
    assert gjtk.validate.is_feature_collection(feature_collection)


def test_is_feature_collection_no_type(feature_collection_without_type):
    """should return false when provided a FeatureCollection object without a type"""
    assert not gjtk.validate.is_feature_collection(feature_collection_without_type)


def test_is_feature_collection_no_features(feature_collection_without_features):
    """should return false when provided a FeatureCollection object without features"""
    assert not gjtk.validate.is_feature_collection(feature_collection_without_features)


def test_is_feature_collection_invalid(types):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.is_feature_collection(types)


def test_is_crs(crs):
    """should return true when provided a valid CRS object"""
    assert gjtk.validate.is_crs(crs)


def test_is_crs_no_type(crs_without_type):
    """should return false when provided a CRS object without a type"""
    assert not gjtk.validate.is_crs(crs_without_type)


def test_is_crs_no_properties(crs_without_properties):
    """should return false when provided a CRS object without properties"""
    assert not gjtk.validate.is_crs(crs_without_properties)


def test_is_crs_invalid(types):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.is_crs(types)


def test_has_crs_geometry(geometry_with_crs):
    """should return true when provided a Geometry with a valid CRS"""
    assert gjtk.validate.has_crs(geometry_with_crs)


def test_has_crs_feature(feature_with_crs):
    """should return true when provided a Feature with a valid CRS"""
    assert gjtk.validate.has_crs(feature_with_crs)


def test_has_crs_feature_collection(feature_collection_with_crs):
    """should return true when provided a FeatureCollection with a valid CRS"""
    assert gjtk.validate.has_crs(feature_collection_with_crs)


def test_has_crs_invalid(immutable):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.has_crs(immutable)


def test_is_link(link):
    """should return true when provided a valid Link object"""
    assert gjtk.validate.is_link(link)


def test_is_link_no_type(link_without_type):
    """should return true when provided a Link object without a type"""
    assert gjtk.validate.is_link(link_without_type)


def test_is_link_no_href(link_without_href):
    """should return false when provided a Link object without href"""
    assert not gjtk.validate.is_link(link_without_href)


def test_is_link_invalid(types):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.is_link(types)


def test_is_bbox(bbox):
    """should return true when provided a valid Bbox"""
    assert gjtk.validate.is_bbox(bbox)


def test_is_bbox_invalid(types):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.is_bbox(types)


def test_is_bbox_malformed(malformed_bbox):
    """should return false when provided a malformed Bbox"""
    assert not gjtk.validate.is_bbox(malformed_bbox)


def test_has_bbox_geometry(geometry_with_bbox):
    """should return true when provided a Geometry with a valid Bbox"""
    assert gjtk.validate.has_bbox(geometry_with_bbox)


def test_has_bbox_feature(feature_with_bbox):
    """should return true when provided a Feature with a valid Bbox"""
    assert gjtk.validate.has_bbox(feature_with_bbox)


def test_has_bbox_feature_collection(feature_collection_with_bbox):
    """should return true when provided a FeatureCollection with a valid Bbox"""
    assert gjtk.validate.has_bbox(feature_collection_with_bbox)


def test_has_bbox_invalid(immutable):
    """should return false when provided an invalid object"""
    assert not gjtk.validate.has_bbox(immutable)


def test_equal_positions(position):
    """should return true when provided identical Positions"""
    assert gjtk.validate.equal_positions(position, position)


def test_equal_positions_unequal(unequal_positions):
    """should return false when provided different Positions"""
    assert not gjtk.validate.equal_positions(unequal_positions[0], unequal_positions[1])
