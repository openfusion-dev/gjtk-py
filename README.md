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

## Methods

Each method takes a single argument unless otherwise noted.

### `gjtk.validate`

All validation methods return `True` or `False`.

#### `isGeoJSON`
returns `True` when passed a valid [GeoJSON object](http://geojson.org/geojson-spec.html#geojson-objects), otherwise `False`

> GeoJSON always consists of a single object. This object (referred to as the GeoJSON object [above]) represents a geometry, feature, or collection of features.

#### `isGeometry`
returns `True` when passed a valid [GeoJSON Geometry](http://geojson.org/geojson-spec.html#geometry-objects), otherwise `False`

> A geometry is a GeoJSON object where the type member's value is one of the following strings: "Point", "MultiPoint", "LineString", "MultiLineString", "Polygon", "MultiPolygon", or "GeometryCollection".

#### `isPosition`
returns `True` when passed a valid [GeoJSON Position](http://geojson.org/geojson-spec.html#positions), otherwise `False`

> A position is represented by an array of numbers. There must be at least two elements, and may be more. The order of elements must follow x, y, z order (easting, northing, altitude for coordinates in a projected coordinate reference system, or longitude, latitude, altitude for coordinates in a geographic coordinate reference system). Any number of additional elements are allowed -- interpretation and meaning of additional elements is beyond the scope of this specification.

#### `isPointCoordinates`
returns `True` when passed valid [GeoJSON Point](http://geojson.org/geojson-spec.html#point) coordinates, otherwise `False`

* example

  ``` json
  [100.0, 0.0]
  ```

#### `isMultiPointCoordinates`
returns `True` when passed valid [GeoJSON MultiPoint](http://geojson.org/geojson-spec.html#multipoint) coordinates, otherwise `False`

* example

    ``` json
    [ [100.0, 0.0], [101.0, 1.0], [102.0, 2.0] ]
    ```

#### `isLineStringCoordinates`
returns `True` when passed valid [GeoJSON LineString](http://geojson.org/geojson-spec.html#linestring) coordinates, otherwise `False`

* example

    ``` json
    [ [100.0, 0.0], [101.0, 1.0] ]
    ```

#### `isLinearRingCoordinates`
returns `True` when passed valid [GeoJSON LinearRing](http://geojson.org/geojson-spec.html#linestring) coordinates, otherwise `False`

> A LinearRing is closed LineString with 4 or more positions. The first and last positions are equivalent (they represent equivalent points). Though a LinearRing is not explicitly represented as a GeoJSON geometry type, it is referred to in the Polygon geometry type definition.

* example

    ``` json
    [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0] ]
    ```

#### `isMultiLineStringCoordinates`
returns `True` when passed valid [GeoJSON MultiLineString](http://geojson.org/geojson-spec.html#multilinestring) coordinates, otherwise `False`

* example

    ``` json
    [
      [ [100.0, 0.0], [101.0, 1.0] ],
      [ [102.0, 2.0], [103.0, 3.0] ]
    ]
    ```

#### `isPolygonCoordinates`
returns `True` when passed valid [GeoJSON Polygon](http://geojson.org/geojson-spec.html#polygon) coordinates, otherwise `False`

* example: 0 holes

    ``` json
    [
      [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0] ]
    ]
    ```

* example: 1 hole

    ``` json
    [
      [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0] ],
      [ [100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8], [100.2, 0.2] ]
    ]
    ```

#### `isMultiPolygonCoordinates`
returns `True` when passed valid [GeoJSON MultiPolygon](http://geojson.org/geojson-spec.html#multipolygon) coordinates, otherwise `False`

* example

    ``` json
    [
      [
        [ [102.0, 2.0], [103.0, 2.0], [103.0, 3.0], [102.0, 3.0], [102.0, 2.0] ]
      ],
      [
        [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0] ],
        [ [100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8], [100.2, 0.2] ]
      ]
    ]
    ```

#### `isPoint`
returns `True` when passed a valid [GeoJSON Point](http://geojson.org/geojson-spec.html#point), otherwise `False`

* example

    ``` json
    { "type": "Point", "coordinates": [100.0, 0.0] }
    ```

#### `isMultiPoint`
returns `True` when passed a valid [GeoJSON MultiPoint](http://geojson.org/geojson-spec.html#multipoint), otherwise `False`

* example

    ``` json
    { "type": "MultiPoint", "coordinates": [ [100.0, 0.0], [101.0, 1.0] ] }
    ```

#### `isLineString`
returns `True` when passed a valid [GeoJSON LineString](http://geojson.org/geojson-spec.html#linestring), otherwise `False`

* example

    ``` json
    {
      "type": "LineString",
      "coordinates": [ [100.0, 0.0], [101.0, 1.0] ]
    }
    ```

#### `isMultiLineString`
returns `True` when passed a valid [GeoJSON MultiLineString](http://geojson.org/geojson-spec.html#multilinestring), otherwise `False`

* example

    ``` json
    {
      "type": "MultiLineString",
      "coordinates": [
        [ [100.0, 0.0], [101.0, 1.0] ],
        [ [102.0, 2.0], [103.0, 3.0] ]
      ]
    }
    ```

#### `isPolygon`
returns `True` when passed a valid [GeoJSON Polygon](http://geojson.org/geojson-spec.html#polygon), otherwise `False`

* example: 0 holes

    ``` json
    {
      "type": "Polygon",
      "coordinates": [
        [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0] ]
      ]
    }
    ```

* example: 1 hole

    ``` json
    {
      "type": "Polygon",
      "coordinates": [
        [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0] ],
        [ [100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8], [100.2, 0.2] ]
      ]
    }
    ```

#### `isMultiPolygon`
returns `True` when passed a valid [GeoJSON MultiPolygon](http://geojson.org/geojson-spec.html#multipolygon), otherwise `False`

* example

    ``` json
    {
      "type": "MultiPolygon",
      "coordinates": [
        [
          [ [102.0, 2.0], [103.0, 2.0], [103.0, 3.0], [102.0, 3.0], [102.0, 2.0] ]
        ],
        [
          [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0] ],
          [ [100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8], [100.2, 0.2] ]
        ]
      ]
    }
    ```

#### `isGeometryCollection`
returns `True` when passed a valid [GeoJSON Geometry Collection](http://geojson.org/geojson-spec.html#geometry-collection), otherwise `False`

* example

    ``` json
    {
      "type": "GeometryCollection",
      "geometries": [
        {
          "type": "Point",
          "coordinates": [100.0, 0.0]
        },
        {
          "type": "LineString",
          "coordinates": [ [101.0, 0.0], [102.0, 1.0] ]
        }
      ]
    }
    ```

#### `isFeature`
returns `True` when passed a valid [GeoJSON Feature](http://geojson.org/geojson-spec.html#feature-objects), otherwise `False`

* example

    ``` json
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [125.6, 10.1]
      },
      "properties": {
        "name": "Dinagat Islands"
      }
    }
    ```

#### `isFeatureCollection`
returns `True` when passed a valid [GeoJSON Feature Collection](http://geojson.org/geojson-spec.html#feature-collection-objects), otherwise `False`

* example

    ``` json
    {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [102.0, 0.5]
          },
          "properties": {
            "prop0": "value0"
          }
        },
        {
          "type": "Feature",
          "geometry": {
            "type": "LineString",
            "coordinates": [ [102.0, 0.0], [103.0, 1.0], [104.0, 0.0], [105.0, 1.0] ]
          },
          "properties": {
            "prop0": "value0",
            "prop1": 0.0
          }
        },
        {
          "type": "Feature",
          "geometry": {
            "type": "Polygon",
            "coordinates": [
              [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0] ]
            ]
          },
          "properties": {
            "prop0": "value0",
            "prop1": {
              "this": "that"
            }
          }
        }
      ]
    }
    ```

#### `isCRS`
returns `True` when passed a valid [GeoJSON Coordinate Reference System](http://geojson.org/geojson-spec.html#coordinate-reference-system-objects), otherwise `False`

* example: [Named CRS](http://geojson.org/geojson-spec.html#named-crs)

    ``` json
    {
      "type": "name",
      "properties": {
        "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
      }
    }
    ```

* example: [Linked CRS](http://geojson.org/geojson-spec.html#linked-crs)

    ``` json
    {
      "type": "link", 
      "properties": {
        "href": "http://example.com/crs/42",
        "type": "proj4"
      }
    }
    ```

#### `hasCRS`
returns `True` when passed an object that validly specifies a [GeoJSON Coordinate Reference System](http://geojson.org/geojson-spec.html#coordinate-reference-system-objects), otherwise `False`

> The coordinate reference system (CRS) of a GeoJSON object is determined by its "crs" member (referred to as the CRS object below). If an object has no crs member, then its parent or grandparent object's crs member may be acquired. If no crs member can be so acquired, the default CRS shall apply to the GeoJSON object.

#### `isLink`
returns `True` when passed a valid [GeoJSON Link](http://geojson.org/geojson-spec.html#link-objects), otherwise `False`

* example

    ``` json
    {
      "type": "link",
      "properties": {
        "href": "data.crs",
        "type": "ogcwkt"
      }
    }
    ```

#### `isBbox`
returns `True` when passed a valid [GeoJSON Bounding Box](http://geojson.org/geojson-spec.html#bounding-boxes), otherwise `False`

* example

    ``` json
    [-180.0, -90.0, 180.0, 90.0]
    ```

#### `hasBbox`
returns `True` when passed an object that validly specifies a [GeoJSON Bounding Box](http://geojson.org/geojson-spec.html#bounding-boxes), otherwise `False`

* example

    ``` json
    {
      "type": "Feature",
      "bbox": [-180.0, -90.0, 180.0, 90.0],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [ [-180.0, 10.0], [20.0, 90.0], [180.0, -5.0], [-30.0, -90.0] ]
        ]
      }
    }
    ```

#### equalPositions(_position1_, _position2_)
returns `True` when all parameters are identical [GeoJSON Positions](http://geojson.org/geojson-spec.html#positions), otherwise `False`

#### containedPolygon(_innerLinearRing_, _outerLinearRing_)
returns `True` when one [GeoJSON LinearRing](http://geojson.org/geojson-spec.html#linestring) contains another, otherwise `False`

### `gjtk.generate`

#### `Point(position)`
returns a random [GeoJSON Point](http://geojson.org/geojson-spec.html#point) object

#### `GeometryCollection(Geometries)`
returns a random [GeoJSON GeometryCollection](http://geojson.org/geojson-spec.html#geometry-collection) object

#### `Feature(Geometry, properties)`
returns a random [GeoJSON Feature](http://geojson.org/geojson-spec.html#feature-objects) object

#### `FeatureCollection(Features)`
returns a random [GeoJSON FeatureCollection](http://geojson.org/geojson-spec.html#feature-collection-objects) object

#### `randomPosition`
returns a random [GeoJSON Position](http://geojson.org/geojson-spec.html#positions) object

#### `randomPointCoordinates`
returns random [GeoJSON Point](http://geojson.org/geojson-spec.html#point) coordinates

#### `randomMultiPointCoordinates`
returns random [GeoJSON MultiPoint](http://geojson.org/geojson-spec.html#multipoint) coordinates

#### `randomLineStringCoordinates`
returns random [GeoJSON LineString](http://geojson.org/geojson-spec.html#linestring) coordinates

#### `randomLinearRingCoordinates`
returns random [GeoJSON LinearRing](http://geojson.org/geojson-spec.html#linestring) coordinates

#### `randomMultiLineStringCoordinates`
returns random [GeoJSON MultiLineString](http://geojson.org/geojson-spec.html#multilinestring) coordinates

#### `randomPolygonCoordinates`
returns random [GeoJSON Polygon](http://geojson.org/geojson-spec.html#polygon) coordinates

#### `randomMultiPolygonCoordinates`
returns random [GeoJSON MultiPolygon](http://geojson.org/geojson-spec.html#multipolygon) coordinates

#### `randomGeometry`
returns a random [GeoJSON Geometry](http://geojson.org/geojson-spec.html#geometry-objects) object

#### `randomPoint`
returns a random [GeoJSON Point](http://geojson.org/geojson-spec.html#point) object

#### `randomMultiPoint`
returns a random [GeoJSON MultiPoint](http://geojson.org/geojson-spec.html#multipoint) object

#### `randomLineString`
returns a random [GeoJSON LineString](http://geojson.org/geojson-spec.html#linestring) object

#### `randomMultiLineString`
returns a random [GeoJSON MultiLineString](http://geojson.org/geojson-spec.html#multilinestring) object

#### `randomPolygon`
returns a random [GeoJSON Polygon](http://geojson.org/geojson-spec.html#polygon) object

#### `randomMultiPolygon`
returns a random [GeoJSON MultiPolygon](http://geojson.org/geojson-spec.html#multipolygon) object

#### `randomGeometryCollection`
returns a random [GeoJSON GeometryCollection](http://geojson.org/geojson-spec.html#geometry-collection) object

#### `randomFeature`
returns a random [GeoJSON Feature](http://geojson.org/geojson-spec.html#feature-objects) object

#### `randomFeatureCollection`
returns a random [GeoJSON FeatureCollection](http://geojson.org/geojson-spec.html#feature-collection-objects) object

#### `randomCRS`
returns a random [GeoJSON Coordinate Reference System](http://geojson.org/geojson-spec.html#coordinate-reference-system-objects) object

#### `randomLink`
returns a random [GeoJSON Link](http://geojson.org/geojson-spec.html#link-objects) object

#### `randomBbox`
returns a random [GeoJSON Bounding Box](http://geojson.org/geojson-spec.html#bounding-boxes) object

### `gjtk.extract`

These methods all take a single argument: a valid [GeoJSON object](http://geojson.org/geojson-spec.html#geojson-objects).

#### `positionsOf`
returns all the Positions in a valid [GeoJSON object](http://geojson.org/geojson-spec.html#geojson-objects)

#### `featuresOf`
returns all the Features in a valid [GeoJSON object](http://geojson.org/geojson-spec.html#geojson-objects)

#### `geometriesOf`
returns all the Geometries in a valid [GeoJSON object](http://geojson.org/geojson-spec.html#geojson-objects)
