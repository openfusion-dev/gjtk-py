GeoJSON ToolKit
===============

``gjtk`` is a library for working with `GeoJSON`_. It aims to be as compliant with the specification (soon `standard`_, hopefully) as possible.

|Build Status| |PyPI Version|

Installation
------------

``gjtk`` is available on `PyPI`_.

.. code:: sh

    pip install gjtk

Usage
-----

.. code:: python

    import gjtk

Modules
-------

``gjtk.extract``
~~~~~~~~~~~~~~~~

+------------------------------+-----------------------------------------------------------+
| Method                       | Description                                               |
+==============================+===========================================================+
| ``positions_of(geojson)``    | returns all the Positions in a valid `GeoJSON object`_    |
+------------------------------+-----------------------------------------------------------+
| ``features_of(geojson)``     | returns all the Features in a valid `GeoJSON object`_     |
+------------------------------+-----------------------------------------------------------+
| ``geometries_of(geojson)``   | returns all the Geometries in a valid `GeoJSON object`_   |
+------------------------------+-----------------------------------------------------------+

``gjtk.generate``
~~~~~~~~~~~~~~~~~

+---------------------------------------+-----------------------------------------+
| Method                                | Description                             |
+=======================================+=========================================+
| ``point(position)``                   | returns a valid `Point`_                |
+---------------------------------------+-----------------------------------------+
| ``multi_point(coordinates)``          | returns a valid `MultiPoint`_           |
+---------------------------------------+-----------------------------------------+
| ``line_string(coordinates)``          | returns a valid `LineString`_           |
+---------------------------------------+-----------------------------------------+
| ``multi_line_string(coordinates)``    | returns a valid `MultiLineString`_      |
+---------------------------------------+-----------------------------------------+
| ``polygon(coordinates)``              | returns a valid `Polygon`_              |
+---------------------------------------+-----------------------------------------+
| ``multi_polygon(coordinates)``        | returns a valid `MultiPolygon`_         |
+---------------------------------------+-----------------------------------------+
| ``geometry_collection(geometries)``   | returns a valid `GeometryCollection`_   |
+---------------------------------------+-----------------------------------------+
| ``feature(geometry, properties)``     | returns a valid `Feature`_              |
+---------------------------------------+-----------------------------------------+
| ``feature_collection(features)``      | returns a valid `FeatureCollection`_    |
+---------------------------------------+-----------------------------------------+

``gjtk.random``
~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------+-------------------------------------------------+
| Method                                                                      | Description                                     |
+=============================================================================+=================================================+
| ``position(max_numbers=3, min_numbers=2)``                                  | returns a random `Position`_                    |
+-----------------------------------------------------------------------------+-------------------------------------------------+
| ``point_coordinates()``                                                     | returns random `Point`_ coordinates             |
+-----------------------------------------------------------------------------+-------------------------------------------------+
| ``multi_point_coordinates(max_positions=6, min_positions=0)``               | returns random `MultiPoint`_ coordinates        |
+-----------------------------------------------------------------------------+-------------------------------------------------+
| ``line_string_coordinates(max_positions=6, min_positions=2)``               | returns random `LineString`_ coordinates        |
+-----------------------------------------------------------------------------+-------------------------------------------------+
| ``linear_ring_coordinates()``                                               | returns random `LinearRing`_ coordinates        |
+-----------------------------------------------------------------------------+-------------------------------------------------+
| ``multi_line_string_coordinates(max_line_strings=6, min_line_strings=1)``   | returns random `MultiLineString`_ coordinates   |
+-----------------------------------------------------------------------------+-------------------------------------------------+
| ``polygon_coordinates()``                                                   | returns random `Polygon`_ coordinates           |
+-----------------------------------------------------------------------------+-------------------------------------------------+
| ``multi_polygon_coordinates(max_polygons=6, min_polygons=1)``               | returns random `MultiPolygon`_ coordinates      |
+-----------------------------------------------------------------------------+-------------------------------------------------+
| ``geometry()``                                                              | returns a random `Geometry`_                    |
+-----------------------------------------------------------------------------+-------------------------------------------------+
| ``point()``                                                                 | returns a random `Point`_                       |
+-----------------------------------------------------------------------------+-------------------------------------------------+
| ``multi_point()``                                                           | returns a random `MultiPoint`_                  |
+-----------------------------------------------------------------------------+-------------------------------------------------+
| ``line_string()``                                                           | returns a random `LineString`_                  |
+-----------------------------------------------------------------------------+-------------------------------------------------+
| ``multi_line_string()``                                                     | returns a random `MultiLineString`_             |
+-----------------------------------------------------------------------------+-------------------------------------------------+
| ``polygon()``                                                               | returns a random `Polygon`_                     |
+-----------------------------------------------------------------------------+-------------------------------------------------+
| ``multi_polygon()``                                                         | returns a random `MultiPolygon`_                |
+-----------------------------------------------------------------------------+-------------------------------------------------+
| ``geometry_collection(max_geometries=3, min_geometries=0)``                 | returns a random `GeometryCollection`_          |
+-----------------------------------------------------------------------------+-------------------------------------------------+
| ``feature()``                                                               | returns a random `Feature`_                     |
+-----------------------------------------------------------------------------+-------------------------------------------------+
| ``feature_collection(max_features=3, min_features=0)``                      | returns a random `FeatureCollection`_           |
+-----------------------------------------------------------------------------+-------------------------------------------------+
| ``crs()``                                                                   | returns a random `CRS`_                         |
+-----------------------------------------------------------------------------+-------------------------------------------------+
| ``link()``                                                                  | returns a random `Link`_                        |
+-----------------------------------------------------------------------------+-------------------------------------------------+
| ``bbox(max_dimensions=4, min_dimensions=2)``                                | returns a random `Bbox`_                        |
+-----------------------------------------------------------------------------+-------------------------------------------------+

``gjtk.validate``
~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| Method                                                    | Description                                                                                              |
+===========================================================+==========================================================================================================+
| ``is_geojson(anything)``                                  | returns ``True`` when passed a valid `GeoJSON object`_, otherwise ``False``                              |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``is_geometry(anything)``                                 | returns ``True`` when passed a valid `Geometry`_, otherwise ``False``                                    |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``is_position(anything)``                                 | returns ``True`` when passed a valid `Position`_, otherwise ``False``                                    |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``is_point_coordinates(anything)``                        | returns ``True`` when passed valid `Point`_ coordinates, otherwise ``False``                             |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``is_multi_point_coordinates(anything)``                  | returns ``True`` when passed valid `MultiPoint`_ coordinates, otherwise ``False``                        |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``is_line_string_coordinates(anything)``                  | returns ``True`` when passed valid `LineString`_ coordinates, otherwise ``False``                        |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``is_linear_ring_coordinates(anything)``                  | returns ``True`` when passed valid `LinearRing`_ coordinates, otherwise ``False``                        |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``is_multi_line_string_coordinates(anything)``            | returns ``True`` when passed valid `MultiLineString`_ coordinates, otherwise ``False``                   |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``is_polygon_coordinates(anything)``                      | returns ``True`` when passed valid `Polygon`_ coordinates, otherwise ``False``                           |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``is_multi_polygon_coordinates(anything)``                | returns ``True`` when passed valid `MultiPolygon`_ coordinates, otherwise ``False``                      |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``is_point(anything)``                                    | returns ``True`` when passed a valid `Point`_, otherwise ``False``                                       |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``is_multi_point(anything)``                              | returns ``True`` when passed a valid `MultiPoint`_, otherwise ``False``                                  |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``is_line_string(anything)``                              | returns ``True`` when passed a valid `LineString`_, otherwise ``False``                                  |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``is_multi_line_string(anything)``                        | returns ``True`` when passed a valid `MultiLineString`_, otherwise ``False``                             |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``is_polygon(anything)``                                  | returns ``True`` when passed a valid `Polygon`_, otherwise ``False``                                     |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``is_multi_polygon(anything)``                            | returns ``True`` when passed a valid `MultiPolygon`_, otherwise ``False``                                |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``is_geometry_collection(anything)``                      | returns ``True`` when passed a valid `GeometryCollection`_, otherwise ``False``                          |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``is_feature(anything)``                                  | returns ``True`` when passed a valid `Feature`_, otherwise ``False``                                     |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``is_feature_collection(anything)``                       | returns ``True`` when passed a valid `Feature Collection`_, otherwise ``False``                          |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``is_crs(anything)``                                      | returns ``True`` when passed a valid `CRS`_, otherwise ``False``                                         |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``has_crs(anything)``                                     | returns ``True`` when passed a `GeoJSON object`_ that validly specifies a `CRS`_, otherwise ``False``    |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``is_link(anything)``                                     | returns ``True`` when passed a valid `Link`_, otherwise ``False``                                        |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``is_bbox(anything)``                                     | returns ``True`` when passed a valid `Bbox`_, otherwise ``False``                                        |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``has_bbox(anything)``                                    | returns ``True`` when passed a `GeoJSON object`_ that validly specifies a `Bbox`_, otherwise ``False``   |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``equal_positions(position1, position2)``                 | returns ``True`` when all parameters are identical `Positions`_, otherwise ``False``                     |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``contained_polygon(innerLinearRing, outerLinearRing)``   | returns ``True`` when one `LinearRing`_ contains another, otherwise ``False``                            |
+-----------------------------------------------------------+----------------------------------------------------------------------------------------------------------+

.. _GeoJSON: http://geojson.org/
.. _standard: https://github.com/geojson/draft-geojson
.. _PyPI: https://pypi.python.org/pypi/gjtk
.. _GeoJSON object: http://geojson.org/geojson-spec.html#geojson-objects
.. _Point: http://geojson.org/geojson-spec.html#point
.. _MultiPoint: http://geojson.org/geojson-spec.html#multipoint
.. _LineString: http://geojson.org/geojson-spec.html#linestring
.. _MultiLineString: http://geojson.org/geojson-spec.html#multilinestring
.. _Polygon: http://geojson.org/geojson-spec.html#polygon
.. _MultiPolygon: http://geojson.org/geojson-spec.html#multipolygon
.. _GeometryCollection: http://geojson.org/geojson-spec.html#geometry-collection
.. _Feature: http://geojson.org/geojson-spec.html#feature-objects
.. _FeatureCollection: http://geojson.org/geojson-spec.html#feature-collection-objects
.. _Position: http://geojson.org/geojson-spec.html#positions
.. _LinearRing: http://geojson.org/geojson-spec.html#linestring
.. _Geometry: http://geojson.org/geojson-spec.html#geometry-objects
.. _CRS: http://geojson.org/geojson-spec.html#coordinate-reference-system-objects
.. _Link: http://geojson.org/geojson-spec.html#link-objects
.. _Bbox: http://geojson.org/geojson-spec.html#bounding-boxes
.. _Feature Collection: http://geojson.org/geojson-spec.html#feature-collection-objects
.. _Positions: http://geojson.org/geojson-spec.html#positions

License
-------

Copyright (C) 2016 David Tucker

This library is free software; you can redistribute it and/or modify it
under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation; either version 2.1 of the License, or (at
your option) any later version.

This library is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser
General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this library; if not, write to the Free Software Foundation,
Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

.. |Build Status| image:: https://img.shields.io/travis/dmtucker/gjtk-py.svg
   :target: https://travis-ci.org/dmtucker/gjtk-py
.. |PyPI Version| image:: https://img.shields.io/pypi/v/gjtk.svg
   :target: https://pypi.python.org/pypi/gjtk
