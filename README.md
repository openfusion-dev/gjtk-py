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

* `Point(position)` returns a valid [GeoJSON Point](http://geojson.org/geojson-spec.html#point)
* `MultiPoint(coordinates)` returns a valid [GeoJSON MultiPoint](http://geojson.org/geojson-spec.html#multipoint)
* `LineString(coordinates)` returns a valid [GeoJSON LineString](http://geojson.org/geojson-spec.html#linestring)
* `MultiLineString(coordinates)` returns a valid [GeoJSON MultiLineString](http://geojson.org/geojson-spec.html#multilinestring)
* `Polygon(coordinates)` returns a valid [GeoJSON Polygon](http://geojson.org/geojson-spec.html#polygon)
* `MultiPolygon(coordinates)` returns a valid [GeoJSON MultiPolygon](http://geojson.org/geojson-spec.html#multipolygon)
* `GeometryCollection(geometries)` returns a valid [GeoJSON GeometryCollection](http://geojson.org/geojson-spec.html#geometry-collection)
* `Feature(geometry, properties)` returns a valid [GeoJSON Feature](http://geojson.org/geojson-spec.html#feature-objects)
* `FeatureCollection(features)` returns a valid [GeoJSON FeatureCollection](http://geojson.org/geojson-spec.html#feature-collection-objects)

### `gjtk.random`

* `Position` returns a random [GeoJSON Position](http://geojson.org/geojson-spec.html#positions)
* `PointCoordinates` returns random [GeoJSON Point](http://geojson.org/geojson-spec.html#point) coordinates
* `MultiPointCoordinates` returns random [GeoJSON MultiPoint](http://geojson.org/geojson-spec.html#multipoint) coordinates
* `LineStringCoordinates` returns random [GeoJSON LineString](http://geojson.org/geojson-spec.html#linestring) coordinates
* `LinearRingCoordinates` returns random [GeoJSON LinearRing](http://geojson.org/geojson-spec.html#linestring) coordinates
* `MultiLineStringCoordinates` returns random [GeoJSON MultiLineString](http://geojson.org/geojson-spec.html#multilinestring) coordinates
* `PolygonCoordinates` returns random [GeoJSON Polygon](http://geojson.org/geojson-spec.html#polygon) coordinates
* `MultiPolygonCoordinates` returns random [GeoJSON MultiPolygon](http://geojson.org/geojson-spec.html#multipolygon) coordinates
* `Geometry` returns a random [GeoJSON Geometry](http://geojson.org/geojson-spec.html#geometry-objects)
* `Point` returns a random [GeoJSON Point](http://geojson.org/geojson-spec.html#point)
* `MultiPoint` returns a random [GeoJSON MultiPoint](http://geojson.org/geojson-spec.html#multipoint)
* `LineString` returns a random [GeoJSON LineString](http://geojson.org/geojson-spec.html#linestring)
* `MultiLineString` returns a random [GeoJSON MultiLineString](http://geojson.org/geojson-spec.html#multilinestring)
* `Polygon` returns a random [GeoJSON Polygon](http://geojson.org/geojson-spec.html#polygon)
* `MultiPolygon` returns a random [GeoJSON MultiPolygon](http://geojson.org/geojson-spec.html#multipolygon)
* `GeometryCollection` returns a random [GeoJSON GeometryCollection](http://geojson.org/geojson-spec.html#geometry-collection)
* `Feature` returns a random [GeoJSON Feature](http://geojson.org/geojson-spec.html#feature-objects)
* `FeatureCollection` returns a random [GeoJSON FeatureCollection](http://geojson.org/geojson-spec.html#feature-collection-objects)
* `CRS` returns a random [GeoJSON Coordinate Reference System](http://geojson.org/geojson-spec.html#coordinate-reference-system-objects)
* `Link` returns a random [GeoJSON Link](http://geojson.org/geojson-spec.html#link-objects)
* `Bbox` returns a random [GeoJSON Bounding Box](http://geojson.org/geojson-spec.html#bounding-boxes)

### `gjtk.validate`

All validation methods return `True` or `False`.

* `isGeoJSON` returns `True` when passed a valid [GeoJSON object](http://geojson.org/geojson-spec.html#geojson-objects), otherwise `False`
* `isGeometry` returns `True` when passed a valid [GeoJSON Geometry](http://geojson.org/geojson-spec.html#geometry-objects), otherwise `False`
* `isPosition` returns `True` when passed a valid [GeoJSON Position](http://geojson.org/geojson-spec.html#positions), otherwise `False`
* `isPointCoordinates` returns `True` when passed valid [GeoJSON Point](http://geojson.org/geojson-spec.html#point) coordinates, otherwise `False`
* `isMultiPointCoordinates` returns `True` when passed valid [GeoJSON MultiPoint](http://geojson.org/geojson-spec.html#multipoint) coordinates, otherwise `False`
* `isLineStringCoordinates` returns `True` when passed valid [GeoJSON LineString](http://geojson.org/geojson-spec.html#linestring) coordinates, otherwise `False`
* `isLinearRingCoordinates` returns `True` when passed valid [GeoJSON LinearRing](http://geojson.org/geojson-spec.html#linestring) coordinates, otherwise `False`
* `isMultiLineStringCoordinates` returns `True` when passed valid [GeoJSON MultiLineString](http://geojson.org/geojson-spec.html#multilinestring) coordinates, otherwise `False`
* `isPolygonCoordinates` returns `True` when passed valid [GeoJSON Polygon](http://geojson.org/geojson-spec.html#polygon) coordinates, otherwise `False`
* `isMultiPolygonCoordinates` returns `True` when passed valid [GeoJSON MultiPolygon](http://geojson.org/geojson-spec.html#multipolygon) coordinates, otherwise `False`
* `isPoint` returns `True` when passed a valid [GeoJSON Point](http://geojson.org/geojson-spec.html#point), otherwise `False`
* `isMultiPoint` returns `True` when passed a valid [GeoJSON MultiPoint](http://geojson.org/geojson-spec.html#multipoint), otherwise `False`
* `isLineString` returns `True` when passed a valid [GeoJSON LineString](http://geojson.org/geojson-spec.html#linestring), otherwise `False`
* `isMultiLineString` returns `True` when passed a valid [GeoJSON MultiLineString](http://geojson.org/geojson-spec.html#multilinestring), otherwise `False`
* `isPolygon` returns `True` when passed a valid [GeoJSON Polygon](http://geojson.org/geojson-spec.html#polygon), otherwise `False`
* `isMultiPolygon` returns `True` when passed a valid [GeoJSON MultiPolygon](http://geojson.org/geojson-spec.html#multipolygon), otherwise `False`
* `isGeometryCollection` returns `True` when passed a valid [GeoJSON Geometry Collection](http://geojson.org/geojson-spec.html#geometry-collection), otherwise `False`
* `isFeature` returns `True` when passed a valid [GeoJSON Feature](http://geojson.org/geojson-spec.html#feature-objects), otherwise `False`
* `isFeatureCollection` returns `True` when passed a valid [GeoJSON Feature Collection](http://geojson.org/geojson-spec.html#feature-collection-objects), otherwise `False`
* `isCRS` returns `True` when passed a valid [GeoJSON Coordinate Reference System](http://geojson.org/geojson-spec.html#coordinate-reference-system-objects), otherwise `False`
* `hasCRS` returns `True` when passed a [GeoJSON object](http://geojson.org/geojson-spec.html#geojson-objects) that validly specifies a [GeoJSON Coordinate Reference System](http://geojson.org/geojson-spec.html#coordinate-reference-system-objects), otherwise `False`
* `isLink` returns `True` when passed a valid [GeoJSON Link](http://geojson.org/geojson-spec.html#link-objects), otherwise `False`
* `isBbox` returns `True` when passed a valid [GeoJSON Bounding Box](http://geojson.org/geojson-spec.html#bounding-boxes), otherwise `False`
* `hasBbox` returns `True` when passed a [GeoJSON object](http://geojson.org/geojson-spec.html#geojson-objects) that validly specifies a [GeoJSON Bounding Box](http://geojson.org/geojson-spec.html#bounding-boxes), otherwise `False`

* `equalPositions(position1, position2)` returns `True` when all parameters are identical [GeoJSON Positions](http://geojson.org/geojson-spec.html#positions), otherwise `False`
* `containedPolygon(innerLinearRing, outerLinearRing)` returns `True` when one [GeoJSON LinearRing](http://geojson.org/geojson-spec.html#linestring) contains another, otherwise `False`
