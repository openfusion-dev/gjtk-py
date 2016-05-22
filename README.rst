GeoJSON ToolKit
===============

``gjtk`` is a library for working with
`GeoJSON <http://geojson.org/>`__. It aims to be as compliant with the
specification (soon
`standard <https://github.com/geojson/draft-geojson>`__, hopefully) as
possible.

|Build Status| |PyPI Version|

Installation
------------

``gjtk`` is available on `PyPI <https://pypi.python.org/pypi/gjtk>`__.

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

+--------------------------+--------------+
| Method                   | Description  |
+==========================+==============+
| ``positionsOf(geojson)`` | returns all  |
|                          | the          |
|                          | Positions in |
|                          | a valid      |
|                          | `GeoJSON     |
|                          | object <http |
|                          | ://geojson.o |
|                          | rg/geojson-s |
|                          | pec.html#geo |
|                          | json-objects |
|                          | >`__         |
+--------------------------+--------------+
| ``featuresOf(geojson)``  | returns all  |
|                          | the Features |
|                          | in a valid   |
|                          | `GeoJSON     |
|                          | object <http |
|                          | ://geojson.o |
|                          | rg/geojson-s |
|                          | pec.html#geo |
|                          | json-objects |
|                          | >`__         |
+--------------------------+--------------+
| ``geometriesOf(geojson)` | returns all  |
| `                        | the          |
|                          | Geometries   |
|                          | in a valid   |
|                          | `GeoJSON     |
|                          | object <http |
|                          | ://geojson.o |
|                          | rg/geojson-s |
|                          | pec.html#geo |
|                          | json-objects |
|                          | >`__         |
+--------------------------+--------------+

``gjtk.generate``
~~~~~~~~~~~~~~~~~

+--------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Method                               | Description                                                                                               |
+======================================+===========================================================================================================+
| ``Point(position)``                  | returns a valid `Point <http://geojson.org/geojson-spec.html#point>`__                                    |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``MultiPoint(coordinates)``          | returns a valid `MultiPoint <http://geojson.org/geojson-spec.html#multipoint>`__                          |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``LineString(coordinates)``          | returns a valid `LineString <http://geojson.org/geojson-spec.html#linestring>`__                          |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``MultiLineString(coordinates)``     | returns a valid `MultiLineString <http://geojson.org/geojson-spec.html#multilinestring>`__                |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``Polygon(coordinates)``             | returns a valid `Polygon <http://geojson.org/geojson-spec.html#polygon>`__                                |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``MultiPolygon(coordinates)``        | returns a valid `MultiPolygon <http://geojson.org/geojson-spec.html#multipolygon>`__                      |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``GeometryCollection(geometries)``   | returns a valid `GeometryCollection <http://geojson.org/geojson-spec.html#geometry-collection>`__         |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``Feature(geometry, properties)``    | returns a valid `Feature <http://geojson.org/geojson-spec.html#feature-objects>`__                        |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``FeatureCollection(features)``      | returns a valid `FeatureCollection <http://geojson.org/geojson-spec.html#feature-collection-objects>`__   |
+--------------------------------------+-----------------------------------------------------------------------------------------------------------+

``gjtk.random``
~~~~~~~~~~~~~~~

+---------------------------------------------------------------+------------+
| Method                                                        | Descriptio |
|                                                               | n          |
+===============================================================+============+
| ``Position(max_numbers=3, min_numbers=2)``                    | returns a  |
|                                                               | random     |
|                                                               | `Position  |
|                                                               | <http://ge |
|                                                               | ojson.org/ |
|                                                               | geojson-sp |
|                                                               | ec.html#po |
|                                                               | sitions>`_ |
|                                                               | _          |
+---------------------------------------------------------------+------------+
| ``PointCoordinates()``                                        | returns    |
|                                                               | random     |
|                                                               | `Point <ht |
|                                                               | tp://geojs |
|                                                               | on.org/geo |
|                                                               | json-spec. |
|                                                               | html#point |
|                                                               | >`__       |
|                                                               | coordinate |
|                                                               | s          |
+---------------------------------------------------------------+------------+
| ``MultiPointCoordinates(max_positions=6, min_positions=0)``   | returns    |
|                                                               | random     |
|                                                               | `MultiPoin |
|                                                               | t <http:// |
|                                                               | geojson.or |
|                                                               | g/geojson- |
|                                                               | spec.html# |
|                                                               | multipoint |
|                                                               | >`__       |
|                                                               | coordinate |
|                                                               | s          |
+---------------------------------------------------------------+------------+
| ``LineStringCoordinates(max_positions=6, min_positions=2)``   | returns    |
|                                                               | random     |
|                                                               | `LineStrin |
|                                                               | g <http:// |
|                                                               | geojson.or |
|                                                               | g/geojson- |
|                                                               | spec.html# |
|                                                               | linestring |
|                                                               | >`__       |
|                                                               | coordinate |
|                                                               | s          |
+---------------------------------------------------------------+------------+
| ``LinearRingCoordinates()``                                   | returns    |
|                                                               | random     |
|                                                               | `LinearRin |
|                                                               | g <http:// |
|                                                               | geojson.or |
|                                                               | g/geojson- |
|                                                               | spec.html# |
|                                                               | linestring |
|                                                               | >`__       |
|                                                               | coordinate |
|                                                               | s          |
+---------------------------------------------------------------+------------+
| ``MultiLineStringCoordinates(max_line_strings=6, min_line_str | returns    |
| ings=1)``                                                     | random     |
|                                                               | `MultiLine |
|                                                               | String <ht |
|                                                               | tp://geojs |
|                                                               | on.org/geo |
|                                                               | json-spec. |
|                                                               | html#multi |
|                                                               | linestring |
|                                                               | >`__       |
|                                                               | coordinate |
|                                                               | s          |
+---------------------------------------------------------------+------------+
| ``PolygonCoordinates()``                                      | returns    |
|                                                               | random     |
|                                                               | `Polygon < |
|                                                               | http://geo |
|                                                               | json.org/g |
|                                                               | eojson-spe |
|                                                               | c.html#pol |
|                                                               | ygon>`__   |
|                                                               | coordinate |
|                                                               | s          |
+---------------------------------------------------------------+------------+
| ``MultiPolygonCoordinates(max_polygons=6, min_polygons=1)``   | returns    |
|                                                               | random     |
|                                                               | `MultiPoly |
|                                                               | gon <http: |
|                                                               | //geojson. |
|                                                               | org/geojso |
|                                                               | n-spec.htm |
|                                                               | l#multipol |
|                                                               | ygon>`__   |
|                                                               | coordinate |
|                                                               | s          |
+---------------------------------------------------------------+------------+
| ``Geometry()``                                                | returns a  |
|                                                               | random     |
|                                                               | `Geometry  |
|                                                               | <http://ge |
|                                                               | ojson.org/ |
|                                                               | geojson-sp |
|                                                               | ec.html#ge |
|                                                               | ometry-obj |
|                                                               | ects>`__   |
+---------------------------------------------------------------+------------+
| ``Point()``                                                   | returns a  |
|                                                               | random     |
|                                                               | `Point <ht |
|                                                               | tp://geojs |
|                                                               | on.org/geo |
|                                                               | json-spec. |
|                                                               | html#point |
|                                                               | >`__       |
+---------------------------------------------------------------+------------+
| ``MultiPoint()``                                              | returns a  |
|                                                               | random     |
|                                                               | `MultiPoin |
|                                                               | t <http:// |
|                                                               | geojson.or |
|                                                               | g/geojson- |
|                                                               | spec.html# |
|                                                               | multipoint |
|                                                               | >`__       |
+---------------------------------------------------------------+------------+
| ``LineString()``                                              | returns a  |
|                                                               | random     |
|                                                               | `LineStrin |
|                                                               | g <http:// |
|                                                               | geojson.or |
|                                                               | g/geojson- |
|                                                               | spec.html# |
|                                                               | linestring |
|                                                               | >`__       |
+---------------------------------------------------------------+------------+
| ``MultiLineString()``                                         | returns a  |
|                                                               | random     |
|                                                               | `MultiLine |
|                                                               | String <ht |
|                                                               | tp://geojs |
|                                                               | on.org/geo |
|                                                               | json-spec. |
|                                                               | html#multi |
|                                                               | linestring |
|                                                               | >`__       |
+---------------------------------------------------------------+------------+
| ``Polygon()``                                                 | returns a  |
|                                                               | random     |
|                                                               | `Polygon < |
|                                                               | http://geo |
|                                                               | json.org/g |
|                                                               | eojson-spe |
|                                                               | c.html#pol |
|                                                               | ygon>`__   |
+---------------------------------------------------------------+------------+
| ``MultiPolygon()``                                            | returns a  |
|                                                               | random     |
|                                                               | `MultiPoly |
|                                                               | gon <http: |
|                                                               | //geojson. |
|                                                               | org/geojso |
|                                                               | n-spec.htm |
|                                                               | l#multipol |
|                                                               | ygon>`__   |
+---------------------------------------------------------------+------------+
| ``GeometryCollection(max_geometries=3, min_geometries=0)``    | returns a  |
|                                                               | random     |
|                                                               | `GeometryC |
|                                                               | ollection  |
|                                                               | <http://ge |
|                                                               | ojson.org/ |
|                                                               | geojson-sp |
|                                                               | ec.html#ge |
|                                                               | ometry-col |
|                                                               | lection>`_ |
|                                                               | _          |
+---------------------------------------------------------------+------------+
| ``Feature()``                                                 | returns a  |
|                                                               | random     |
|                                                               | `Feature < |
|                                                               | http://geo |
|                                                               | json.org/g |
|                                                               | eojson-spe |
|                                                               | c.html#fea |
|                                                               | ture-objec |
|                                                               | ts>`__     |
+---------------------------------------------------------------+------------+
| ``FeatureCollection(max_features=3, min_features=0)``         | returns a  |
|                                                               | random     |
|                                                               | `FeatureCo |
|                                                               | llection < |
|                                                               | http://geo |
|                                                               | json.org/g |
|                                                               | eojson-spe |
|                                                               | c.html#fea |
|                                                               | ture-colle |
|                                                               | ction-obje |
|                                                               | cts>`__    |
+---------------------------------------------------------------+------------+
| ``CRS()``                                                     | returns a  |
|                                                               | random     |
|                                                               | `CRS <http |
|                                                               | ://geojson |
|                                                               | .org/geojs |
|                                                               | on-spec.ht |
|                                                               | ml#coordin |
|                                                               | ate-refere |
|                                                               | nce-system |
|                                                               | -objects>` |
|                                                               | __         |
+---------------------------------------------------------------+------------+
| ``Link()``                                                    | returns a  |
|                                                               | random     |
|                                                               | `Link <htt |
|                                                               | p://geojso |
|                                                               | n.org/geoj |
|                                                               | son-spec.h |
|                                                               | tml#link-o |
|                                                               | bjects>`__ |
+---------------------------------------------------------------+------------+
| ``Bbox(max_dimensions=4, min_dimensions=2)``                  | returns a  |
|                                                               | random     |
|                                                               | `Bbox <htt |
|                                                               | p://geojso |
|                                                               | n.org/geoj |
|                                                               | son-spec.h |
|                                                               | tml#boundi |
|                                                               | ng-boxes>` |
|                                                               | __         |
+---------------------------------------------------------------+------------+

``gjtk.validate``
~~~~~~~~~~~~~~~~~

+-------------------------------------------------------+--------------+
| Method                                                | Description  |
+=======================================================+==============+
| ``isGeoJSON(anything)``                               | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | a valid      |
|                                                       | `GeoJSON     |
|                                                       | object <http |
|                                                       | ://geojson.o |
|                                                       | rg/geojson-s |
|                                                       | pec.html#geo |
|                                                       | json-objects |
|                                                       | >`__,        |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``isGeometry(anything)``                              | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | a valid      |
|                                                       | `Geometry <h |
|                                                       | ttp://geojso |
|                                                       | n.org/geojso |
|                                                       | n-spec.html# |
|                                                       | geometry-obj |
|                                                       | ects>`__,    |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``isPosition(anything)``                              | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | a valid      |
|                                                       | `Position <h |
|                                                       | ttp://geojso |
|                                                       | n.org/geojso |
|                                                       | n-spec.html# |
|                                                       | positions>`_ |
|                                                       | _,           |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``isPointCoordinates(anything)``                      | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | valid        |
|                                                       | `Point <http |
|                                                       | ://geojson.o |
|                                                       | rg/geojson-s |
|                                                       | pec.html#poi |
|                                                       | nt>`__       |
|                                                       | coordinates, |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``isMultiPointCoordinates(anything)``                 | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | valid        |
|                                                       | `MultiPoint  |
|                                                       | <http://geoj |
|                                                       | son.org/geoj |
|                                                       | son-spec.htm |
|                                                       | l#multipoint |
|                                                       | >`__         |
|                                                       | coordinates, |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``isLineStringCoordinates(anything)``                 | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | valid        |
|                                                       | `LineString  |
|                                                       | <http://geoj |
|                                                       | son.org/geoj |
|                                                       | son-spec.htm |
|                                                       | l#linestring |
|                                                       | >`__         |
|                                                       | coordinates, |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``isLinearRingCoordinates(anything)``                 | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | valid        |
|                                                       | `LinearRing  |
|                                                       | <http://geoj |
|                                                       | son.org/geoj |
|                                                       | son-spec.htm |
|                                                       | l#linestring |
|                                                       | >`__         |
|                                                       | coordinates, |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``isMultiLineStringCoordinates(anything)``            | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | valid        |
|                                                       | `MultiLineSt |
|                                                       | ring <http:/ |
|                                                       | /geojson.org |
|                                                       | /geojson-spe |
|                                                       | c.html#multi |
|                                                       | linestring>` |
|                                                       | __           |
|                                                       | coordinates, |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``isPolygonCoordinates(anything)``                    | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | valid        |
|                                                       | `Polygon <ht |
|                                                       | tp://geojson |
|                                                       | .org/geojson |
|                                                       | -spec.html#p |
|                                                       | olygon>`__   |
|                                                       | coordinates, |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``isMultiPolygonCoordinates(anything)``               | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | valid        |
|                                                       | `MultiPolygo |
|                                                       | n <http://ge |
|                                                       | ojson.org/ge |
|                                                       | ojson-spec.h |
|                                                       | tml#multipol |
|                                                       | ygon>`__     |
|                                                       | coordinates, |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``isPoint(anything)``                                 | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | a valid      |
|                                                       | `Point <http |
|                                                       | ://geojson.o |
|                                                       | rg/geojson-s |
|                                                       | pec.html#poi |
|                                                       | nt>`__,      |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``isMultiPoint(anything)``                            | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | a valid      |
|                                                       | `MultiPoint  |
|                                                       | <http://geoj |
|                                                       | son.org/geoj |
|                                                       | son-spec.htm |
|                                                       | l#multipoint |
|                                                       | >`__,        |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``isLineString(anything)``                            | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | a valid      |
|                                                       | `LineString  |
|                                                       | <http://geoj |
|                                                       | son.org/geoj |
|                                                       | son-spec.htm |
|                                                       | l#linestring |
|                                                       | >`__,        |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``isMultiLineString(anything)``                       | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | a valid      |
|                                                       | `MultiLineSt |
|                                                       | ring <http:/ |
|                                                       | /geojson.org |
|                                                       | /geojson-spe |
|                                                       | c.html#multi |
|                                                       | linestring>` |
|                                                       | __,          |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``isPolygon(anything)``                               | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | a valid      |
|                                                       | `Polygon <ht |
|                                                       | tp://geojson |
|                                                       | .org/geojson |
|                                                       | -spec.html#p |
|                                                       | olygon>`__,  |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``isMultiPolygon(anything)``                          | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | a valid      |
|                                                       | `MultiPolygo |
|                                                       | n <http://ge |
|                                                       | ojson.org/ge |
|                                                       | ojson-spec.h |
|                                                       | tml#multipol |
|                                                       | ygon>`__,    |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``isGeometryCollection(anything)``                    | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | a valid      |
|                                                       | `GeometryCol |
|                                                       | lection <htt |
|                                                       | p://geojson. |
|                                                       | org/geojson- |
|                                                       | spec.html#ge |
|                                                       | ometry-colle |
|                                                       | ction>`__,   |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``isFeature(anything)``                               | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | a valid      |
|                                                       | `Feature <ht |
|                                                       | tp://geojson |
|                                                       | .org/geojson |
|                                                       | -spec.html#f |
|                                                       | eature-objec |
|                                                       | ts>`__,      |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``isFeatureCollection(anything)``                     | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | a valid      |
|                                                       | `Feature     |
|                                                       | Collection < |
|                                                       | http://geojs |
|                                                       | on.org/geojs |
|                                                       | on-spec.html |
|                                                       | #feature-col |
|                                                       | lection-obje |
|                                                       | cts>`__,     |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``isCRS(anything)``                                   | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | a valid      |
|                                                       | `CRS <http:/ |
|                                                       | /geojson.org |
|                                                       | /geojson-spe |
|                                                       | c.html#coord |
|                                                       | inate-refere |
|                                                       | nce-system-o |
|                                                       | bjects>`__,  |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``hasCRS(anything)``                                  | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | a `GeoJSON   |
|                                                       | object <http |
|                                                       | ://geojson.o |
|                                                       | rg/geojson-s |
|                                                       | pec.html#geo |
|                                                       | json-objects |
|                                                       | >`__         |
|                                                       | that validly |
|                                                       | specifies a  |
|                                                       | `CRS <http:/ |
|                                                       | /geojson.org |
|                                                       | /geojson-spe |
|                                                       | c.html#coord |
|                                                       | inate-refere |
|                                                       | nce-system-o |
|                                                       | bjects>`__,  |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``isLink(anything)``                                  | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | a valid      |
|                                                       | `Link <http: |
|                                                       | //geojson.or |
|                                                       | g/geojson-sp |
|                                                       | ec.html#link |
|                                                       | -objects>`__ |
|                                                       | ,            |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``isBbox(anything)``                                  | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | a valid      |
|                                                       | `Bbox <http: |
|                                                       | //geojson.or |
|                                                       | g/geojson-sp |
|                                                       | ec.html#boun |
|                                                       | ding-boxes>` |
|                                                       | __,          |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``hasBbox(anything)``                                 | returns      |
|                                                       | ``True``     |
|                                                       | when passed  |
|                                                       | a `GeoJSON   |
|                                                       | object <http |
|                                                       | ://geojson.o |
|                                                       | rg/geojson-s |
|                                                       | pec.html#geo |
|                                                       | json-objects |
|                                                       | >`__         |
|                                                       | that validly |
|                                                       | specifies a  |
|                                                       | `Bbox <http: |
|                                                       | //geojson.or |
|                                                       | g/geojson-sp |
|                                                       | ec.html#boun |
|                                                       | ding-boxes>` |
|                                                       | __,          |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``equalPositions(position1, position2)``              | returns      |
|                                                       | ``True``     |
|                                                       | when all     |
|                                                       | parameters   |
|                                                       | are          |
|                                                       | identical    |
|                                                       | `Positions < |
|                                                       | http://geojs |
|                                                       | on.org/geojs |
|                                                       | on-spec.html |
|                                                       | #positions>` |
|                                                       | __,          |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+
| ``containedPolygon(innerLinearRing, outerLinearRing)` | returns      |
| `                                                     | ``True``     |
|                                                       | when one     |
|                                                       | `LinearRing  |
|                                                       | <http://geoj |
|                                                       | son.org/geoj |
|                                                       | son-spec.htm |
|                                                       | l#linestring |
|                                                       | >`__         |
|                                                       | contains     |
|                                                       | another,     |
|                                                       | otherwise    |
|                                                       | ``False``    |
+-------------------------------------------------------+--------------+

.. |Build Status| image:: https://img.shields.io/codeship/68395630-1c40-0133-3824-627b75fb3d39/master.svg
   :target: https://codeship.com/projects/94661
.. |PyPI Version| image:: https://img.shields.io/pypi/v/gjtk.svg
   :target: https://pypi.python.org/pypi/gjtk
