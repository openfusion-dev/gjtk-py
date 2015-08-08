# GeoJSON ToolKit

`gjtk` is a library for working with [GeoJSON](http://geojson.org/).
It aims to be as compliant with the specification (soon [standard](https://github.com/geojson/draft-geojson), hopefully) as possible.

[![Build Status](https://img.shields.io/codeship/68395630-1c40-0133-3824-627b75fb3d39/master.svg)](https://codeship.com/projects/94661)
[![PyPI Version](https://img.shields.io/pypi/v/gjtk.svg)](https://pypi.python.org/pypi/gjtk)

## Installation

`gjtk` is available on [PyPI](https://pypi.python.org/pypi/gjtk).

``` sh
pip install gjtk
```

## Usage

``` python
import gjtk
```

## Modules

### `gjtk.extract`

* `positionsOf(geojson)` returns all the Positions in a valid [GeoJSON object](http://geojson.org/geojson-spec.html#geojson-objects)
* `featuresOf(geojson)` returns all the Features in a valid [GeoJSON object](http://geojson.org/geojson-spec.html#geojson-objects)
* `geometriesOf(geojson)` returns all the Geometries in a valid [GeoJSON object](http://geojson.org/geojson-spec.html#geojson-objects)

### `gjtk.generate`

* `Point(position)` returns a valid [Point](http://geojson.org/geojson-spec.html#point)
* `MultiPoint(coordinates)` returns a valid [MultiPoint](http://geojson.org/geojson-spec.html#multipoint)
* `LineString(coordinates)` returns a valid [LineString](http://geojson.org/geojson-spec.html#linestring)
* `MultiLineString(coordinates)` returns a valid [MultiLineString](http://geojson.org/geojson-spec.html#multilinestring)
* `Polygon(coordinates)` returns a valid [Polygon](http://geojson.org/geojson-spec.html#polygon)
* `MultiPolygon(coordinates)` returns a valid [MultiPolygon](http://geojson.org/geojson-spec.html#multipolygon)
* `GeometryCollection(geometries)` returns a valid [GeometryCollection](http://geojson.org/geojson-spec.html#geometry-collection)
* `Feature(geometry, properties)` returns a valid [Feature](http://geojson.org/geojson-spec.html#feature-objects)
* `FeatureCollection(features)` returns a valid [FeatureCollection](http://geojson.org/geojson-spec.html#feature-collection-objects)

### `gjtk.random`

* *`Position(max_numbers=3, min_numbers=2)`* returns a random [Position](http://geojson.org/geojson-spec.html#positions)
* `PointCoordinates()` returns random [Point](http://geojson.org/geojson-spec.html#point) coordinates
* `MultiPointCoordinates(max_positions=6, min_positions=0)` returns random [MultiPoint](http://geojson.org/geojson-spec.html#multipoint) coordinates
* `LineStringCoordinates(max_positions=6, min_positions=2)` returns random [LineString](http://geojson.org/geojson-spec.html#linestring) coordinates
* `LinearRingCoordinates()` returns random [LinearRing](http://geojson.org/geojson-spec.html#linestring) coordinates
* `MultiLineStringCoordinates(max_line_strings=6, min_line_strings=1)` returns random [MultiLineString](http://geojson.org/geojson-spec.html#multilinestring) coordinates
* `PolygonCoordinates()` returns random [Polygon](http://geojson.org/geojson-spec.html#polygon) coordinates
* `MultiPolygonCoordinates(max_polygons=6, min_polygons=1)` returns random [MultiPolygon](http://geojson.org/geojson-spec.html#multipolygon) coordinates
* `Geometry()` returns a random [Geometry](http://geojson.org/geojson-spec.html#geometry-objects)
* `Point()` returns a random [Point](http://geojson.org/geojson-spec.html#point)
* `MultiPoint()` returns a random [MultiPoint](http://geojson.org/geojson-spec.html#multipoint)
* `LineString()` returns a random [LineString](http://geojson.org/geojson-spec.html#linestring)
* `MultiLineString()` returns a random [MultiLineString](http://geojson.org/geojson-spec.html#multilinestring)
* `Polygon()` returns a random [Polygon](http://geojson.org/geojson-spec.html#polygon)
* `MultiPolygon()` returns a random [MultiPolygon](http://geojson.org/geojson-spec.html#multipolygon)
* `GeometryCollection(max_geometries=3, min_geometries=0)` returns a random [GeometryCollection](http://geojson.org/geojson-spec.html#geometry-collection)
* `Feature()` returns a random [Feature](http://geojson.org/geojson-spec.html#feature-objects)
* `FeatureCollection(max_features=3, min_features=0)` returns a random [FeatureCollection](http://geojson.org/geojson-spec.html#feature-collection-objects)
* `CRS()` returns a random [CRS](http://geojson.org/geojson-spec.html#coordinate-reference-system-objects)
* `Link)` returns a random [Link](http://geojson.org/geojson-spec.html#link-objects)
* `Bbox(max_dimensions=4, min_dimensions=2)` returns a random [Bbox](http://geojson.org/geojson-spec.html#bounding-boxes)

### `gjtk.validate`

All validation methods return `True` or `False`.

* `isGeoJSON(anything)` returns `True` when passed a valid [GeoJSON object](http://geojson.org/geojson-spec.html#geojson-objects), otherwise `False`
* `isGeometry(anything)` returns `True` when passed a valid [Geometry](http://geojson.org/geojson-spec.html#geometry-objects), otherwise `False`
* `isPosition(anything)` returns `True` when passed a valid [Position](http://geojson.org/geojson-spec.html#positions), otherwise `False`
* `isPointCoordinates(anything)` returns `True` when passed valid [Point](http://geojson.org/geojson-spec.html#point) coordinates, otherwise `False`
* `isMultiPointCoordinates(anything)` returns `True` when passed valid [MultiPoint](http://geojson.org/geojson-spec.html#multipoint) coordinates, otherwise `False`
* `isLineStringCoordinates(anything)` returns `True` when passed valid [LineString](http://geojson.org/geojson-spec.html#linestring) coordinates, otherwise `False`
* `isLinearRingCoordinates(anything)` returns `True` when passed valid [LinearRing](http://geojson.org/geojson-spec.html#linestring) coordinates, otherwise `False`
* `isMultiLineStringCoordinates(anything)` returns `True` when passed valid [MultiLineString](http://geojson.org/geojson-spec.html#multilinestring) coordinates, otherwise `False`
* `isPolygonCoordinates(anything)` returns `True` when passed valid [Polygon](http://geojson.org/geojson-spec.html#polygon) coordinates, otherwise `False`
* `isMultiPolygonCoordinates(anything)` returns `True` when passed valid [MultiPolygon](http://geojson.org/geojson-spec.html#multipolygon) coordinates, otherwise `False`
* `isPoint(anything)` returns `True` when passed a valid [Point](http://geojson.org/geojson-spec.html#point), otherwise `False`
* `isMultiPoint(anything)` returns `True` when passed a valid [MultiPoint](http://geojson.org/geojson-spec.html#multipoint), otherwise `False`
* `isLineString(anything)` returns `True` when passed a valid [LineString](http://geojson.org/geojson-spec.html#linestring), otherwise `False`
* `isMultiLineString(anything)` returns `True` when passed a valid [MultiLineString](http://geojson.org/geojson-spec.html#multilinestring), otherwise `False`
* `isPolygon(anything)` returns `True` when passed a valid [Polygon](http://geojson.org/geojson-spec.html#polygon), otherwise `False`
* `isMultiPolygon(anything)` returns `True` when passed a valid [MultiPolygon](http://geojson.org/geojson-spec.html#multipolygon), otherwise `False`
* `isGeometryCollection(anything)` returns `True` when passed a valid [GeometryCollection](http://geojson.org/geojson-spec.html#geometry-collection), otherwise `False`
* `isFeature(anything)` returns `True` when passed a valid [Feature](http://geojson.org/geojson-spec.html#feature-objects), otherwise `False`
* `isFeatureCollection(anything)` returns `True` when passed a valid [Feature Collection](http://geojson.org/geojson-spec.html#feature-collection-objects), otherwise `False`
* `isCRS(anything)` returns `True` when passed a valid [CRS](http://geojson.org/geojson-spec.html#coordinate-reference-system-objects), otherwise `False`
* `hasCRS(anything)` returns `True` when passed a [GeoJSON object](http://geojson.org/geojson-spec.html#geojson-objects) that validly specifies a [CRS](http://geojson.org/geojson-spec.html#coordinate-reference-system-objects), otherwise `False`
* `isLink(anything)` returns `True` when passed a valid [Link](http://geojson.org/geojson-spec.html#link-objects), otherwise `False`
* `isBbox(anything)` returns `True` when passed a valid [Bbox](http://geojson.org/geojson-spec.html#bounding-boxes), otherwise `False`
* `hasBbox(anything)` returns `True` when passed a [GeoJSON object](http://geojson.org/geojson-spec.html#geojson-objects) that validly specifies a [Bbox](http://geojson.org/geojson-spec.html#bounding-boxes), otherwise `False`
* `equalPositions(position1, position2)` returns `True` when all parameters are identical [Positions](http://geojson.org/geojson-spec.html#positions), otherwise `False`
* `containedPolygon(innerLinearRing, outerLinearRing)` returns `True` when one [LinearRing](http://geojson.org/geojson-spec.html#linestring) contains another, otherwise `False`
