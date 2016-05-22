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

+--------------------------------+--------------------+
| Method                         | Description        |
+================================+====================+
| ``positions_of(geojson)``      | returns all the    |
|                                | Positions in a     |
|                                | valid GeoJSON      |
|                                | object <http       |
|                                | ://geojson.o       |
|                                | rg/geojson-s       |
|                                | pec.html#geo       |
|                                | json-objects >\_\_ |
+--------------------------------+--------------------+
| ``features_of(geojson)``       | returns all the    |
|                                | Features in a      |
|                                | valid GeoJSON      |
|                                | object <http       |
|                                | ://geojson.o       |
|                                | rg/geojson-s       |
|                                | pec.html#geo       |
|                                | json-objects >\_\_ |
+--------------------------------+--------------------+
| \`geometries\_of(geojson) \`   | returns all the    |
|                                | Geometries in a    |
|                                | valid GeoJSON      |
|                                | object <http%20    |
|                                | ://geojson.o%20    |
|                                | rg/geojson-s%20    |
|                                | pec.html#geo%20    |
|                                | json-objects>\_ \_ |
+--------------------------------+--------------------+

``gjtk.generate``
~~~~~~~~~~~~~~~~~

+----------------------+-----------------------------------------------------+
| Method               | Description                                         |
+======================+=====================================================+
| ``point(position)``  | returns a valid                                     |
|                      | Point <http://geojson.org/geojson-spec.html#point>  |
|                      | \_\_                                                |
+----------------------+-----------------------------------------------------+
| ``multi_point(coordi | returns a valid                                     |
|  nates)``            | `MultiPoint <http://geojson.org/geojson-spec.html#m |
|                      | u%20ltipoint>`__                                    |
+----------------------+-----------------------------------------------------+
| ``line_string(coordi | returns a valid                                     |
|  nates)``            | `LineString <http://geojson.org/geojson-spec.html#l |
|                      | i%20nestring>`__                                    |
+----------------------+-----------------------------------------------------+
| ``multi_line_string( | \| returns a valid                                  |
| c oordinates)``      | MultiLineString <http://geojson.org/geojson-spec.ht |
|                      | ml#multilinestring>\_\_                             |
+----------------------+-----------------------------------------------------+
| ``polygon(coordinat  | returns a valid                                     |
| es)``                | Polygon <http://geojson.org/geojson-spec.html#polyg |
|                      | on>\_\_                                             |
+----------------------+-----------------------------------------------------+
| ``multi_polygon(coor | returns a valid                                     |
|  dinates)``          | `MultiPolygon <http://geojson.org/geojson-spec.html |
|                      | #%20multipolygon>`__                                |
+----------------------+-----------------------------------------------------+
| ``geometry_collectio | returns a valid                                     |
|  n(geometries)``     | `GeometryCollection <http://geojson.org/geojson-spe |
|                      | c%20.html#geometry-collection>`__                   |
+----------------------+-----------------------------------------------------+
| ``feature(geometry,  | returns a valid                                     |
|  properties)``       | Feature <http://geojson.org/geojson-spec.html#featu |
|                      | re-objects>\_\_                                     |
+----------------------+-----------------------------------------------------+
| ``feature_collection | returns a valid                                     |
|  (features)``        | `FeatureCollection <http://geojson.org/geojson-spec |
|                      | .%20html#feature-collection-objects>`__             |
+----------------------+-----------------------------------------------------+

``gjtk.random``
~~~~~~~~~~~~~~~

+-----------------------------------------------------------+----------------+
| Method                                                    | Descriptio n   |
+===========================================================+================+
| ``position(max_numbers=3, min_numbers=2)``                | returns a      |
|                                                           | random         |
|                                                           | Position       |
|                                                           | <http://ge     |
|                                                           | ojson.org/     |
|                                                           | geojson-sp     |
|                                                           | ec.html#po     |
|                                                           | sitions>\_ \_  |
+-----------------------------------------------------------+----------------+
| ``point_coordinates()``                                   | returns random |
|                                                           | Point <ht      |
|                                                           | tp://geojs     |
|                                                           | on.org/geo     |
|                                                           | json-spec.     |
|                                                           | html#point     |
|                                                           | >\_\_          |
|                                                           | coordinate s   |
+-----------------------------------------------------------+----------------+
| ``multi_point_coordinates(max_positions=6, min_positions= | \| returns     |
| 0)``                                                      | random         |
|                                                           | MultiPoin t    |
|                                                           | <http://       |
|                                                           | geojson.or     |
|                                                           | g/geojson-spec |
|                                                           | .html#         |
|                                                           | multipoint     |
|                                                           | >\_\_          |
|                                                           | coordinate s   |
+-----------------------------------------------------------+----------------+
| ``line_string_coordinates(max_positions=6, min_positions= | \| returns     |
| 2)``                                                      | random         |
|                                                           | LineStrin g    |
|                                                           | <http://       |
|                                                           | geojson.or     |
|                                                           | g/geojson-spec |
|                                                           | .html#         |
|                                                           | linestring     |
|                                                           | >\_\_          |
|                                                           | coordinate s   |
+-----------------------------------------------------------+----------------+
| ``linear_ring_coordinates()``                             | \| returns     |
|                                                           | random         |
|                                                           | LinearRin g    |
|                                                           | <http://       |
|                                                           | geojson.or     |
|                                                           | g/geojson-spec |
|                                                           | .html#         |
|                                                           | linestring     |
|                                                           | >\_\_          |
|                                                           | coordinate s   |
+-----------------------------------------------------------+----------------+
| ``multi_line_string_coordinates(max_line_strings=6, min_l | s \| returns   |
| ine_ tr ings=1)``                                         |     random     |
|                                                           |     MultiLine  |
|                                                           |     String <ht |
|                                                           |     tp://geojs |
|                                                           |     on.org/geo |
|                                                           |     json-spec. |
|                                                           |     html#multi |
|                                                           |     linestring |
|                                                           |     >\_\_      |
|                                                           |     coordinate |
|                                                           |     s          |
+-----------------------------------------------------------+----------------+
| ``polygon_coordinates()``                                 | returns random |
|                                                           | Polygon <      |
|                                                           | http://geo     |
|                                                           | json.org/g     |
|                                                           | eojson-spe     |
|                                                           | c.html#pol     |
|                                                           | ygon>\_\_      |
|                                                           | coordinate s   |
+-----------------------------------------------------------+----------------+
| ``multi_polygon_coordinates(max_polygons=6, min_polygons= | \| returns     |
| 1)``                                                      | random         |
|                                                           | MultiPoly gon  |
|                                                           | <http:         |
|                                                           | //geojson.     |
|                                                           | org/geojso     |
|                                                           | n-spec.htm     |
|                                                           | l#multipol     |
|                                                           | ygon>\_\_      |
|                                                           | coordinate s   |
+-----------------------------------------------------------+----------------+
| ``geometry()``                                            | returns a      |
|                                                           | random         |
|                                                           | Geometry       |
|                                                           | <http://ge     |
|                                                           | ojson.org/     |
|                                                           | geojson-sp     |
|                                                           | ec.html#ge     |
|                                                           | ometry-obj     |
|                                                           | ects>\_\_      |
+-----------------------------------------------------------+----------------+
| ``point()``                                               | returns a      |
|                                                           | random Point   |
|                                                           | <ht tp://geojs |
|                                                           | on.org/geo     |
|                                                           | json-spec.     |
|                                                           | html#point     |
|                                                           | >\_\_          |
+-----------------------------------------------------------+----------------+
| ``multi_point()``                                         | returns a      |
|                                                           | random         |
|                                                           | MultiPoin t    |
|                                                           | <http://       |
|                                                           | geojson.or     |
|                                                           | g/geojson-     |
|                                                           | spec.html#     |
|                                                           | multipoint     |
|                                                           | >\_\_          |
+-----------------------------------------------------------+----------------+
| ``line_string()``                                         | returns a      |
|                                                           | random         |
|                                                           | LineStrin g    |
|                                                           | <http://       |
|                                                           | geojson.or     |
|                                                           | g/geojson-     |
|                                                           | spec.html#     |
|                                                           | linestring     |
|                                                           | >\_\_          |
+-----------------------------------------------------------+----------------+
| ``multi_line_string()``                                   | \| returns a   |
|                                                           | random         |
|                                                           | MultiLine      |
|                                                           | String <ht     |
|                                                           | tp://geojs     |
|                                                           | on.org/geo     |
|                                                           | json-spec.     |
|                                                           | html#multi     |
|                                                           | linestring     |
|                                                           | >\_\_          |
+-----------------------------------------------------------+----------------+
| ``polygon()``                                             | returns a      |
|                                                           | random Polygon |
|                                                           | < http://geo   |
|                                                           | json.org/g     |
|                                                           | eojson-spe     |
|                                                           | c.html#pol     |
|                                                           | ygon>\_\_      |
+-----------------------------------------------------------+----------------+
| ``multi_polygon()``                                       | returns a      |
|                                                           | random         |
|                                                           | MultiPoly gon  |
|                                                           | <http:         |
|                                                           | //geojson.     |
|                                                           | org/geojso     |
|                                                           | n-spec.htm     |
|                                                           | l#multipol     |
|                                                           | ygon>\_\_      |
+-----------------------------------------------------------+----------------+
| ``geometry_collection(max_geometries=3, min_geometries=0) | returns a      |
| ``                                                        | random         |
|                                                           | GeometryC      |
|                                                           | ollection      |
|                                                           | <http://ge     |
|                                                           | ojson.org/     |
|                                                           | geojson-sp     |
|                                                           | ec.html#ge     |
|                                                           | ometry-col     |
|                                                           | lection>\_ \_  |
+-----------------------------------------------------------+----------------+
| ``feature()``                                             | returns a      |
|                                                           | random Feature |
|                                                           | < http://geo   |
|                                                           | json.org/g     |
|                                                           | eojson-spe     |
|                                                           | c.html#fea     |
|                                                           | ture-objec     |
|                                                           | ts>\_\_        |
+-----------------------------------------------------------+----------------+
| ``feature_collection(max_features=3, min_features=0)``    | returns a      |
|                                                           | random         |
|                                                           | FeatureCo      |
|                                                           | llection <     |
|                                                           | http://geo     |
|                                                           | json.org/g     |
|                                                           | eojson-spe     |
|                                                           | c.html#fea     |
|                                                           | ture-colle     |
|                                                           | ction-obje     |
|                                                           | cts>\_\_       |
+-----------------------------------------------------------+----------------+
| ``crs()``                                                 | returns a      |
|                                                           | random CRS     |
|                                                           | <http          |
|                                                           | ://geojson     |
|                                                           | .org/geojs     |
|                                                           | on-spec.ht     |
|                                                           | ml#coordin     |
|                                                           | ate-refere     |
|                                                           | nce-system     |
|                                                           | -objects> \_\_ |
+-----------------------------------------------------------+----------------+
| ``link()``                                                | returns a      |
|                                                           | random Link    |
|                                                           | <htt           |
|                                                           | p://geojso     |
|                                                           | n.org/geoj     |
|                                                           | son-spec.h     |
|                                                           | tml#link-o     |
|                                                           | bjects>\_\_    |
+-----------------------------------------------------------+----------------+
| ``bbox(max_dimensions=4, min_dimensions=2)``              | returns a      |
|                                                           | random Bbox    |
|                                                           | <htt           |
|                                                           | p://geojso     |
|                                                           | n.org/geoj     |
|                                                           | son-spec.h     |
|                                                           | tml#boundi     |
|                                                           | ng-boxes> \_\_ |
+-----------------------------------------------------------+----------------+

``gjtk.validate``
~~~~~~~~~~~~~~~~~

+---------------------------------------------------------+------------------+
| Method                                                  | Description      |
+=========================================================+==================+
| ``is_geojson(anything)``                                | returns ``True`` |
|                                                         | when passed a    |
|                                                         | valid GeoJSON    |
|                                                         | object <http     |
|                                                         | ://geojson.o     |
|                                                         | rg/geojson-s     |
|                                                         | pec.html#geo     |
|                                                         | json-objects     |
|                                                         | >\_\_, otherwise |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``is_geometry(anything)``                               | returns ``True`` |
|                                                         | when passed a    |
|                                                         | valid Geometry   |
|                                                         | <h ttp://geojso  |
|                                                         | n.org/geojso     |
|                                                         | n-spec.html#     |
|                                                         | geometry-obj     |
|                                                         | ects>\_\_,       |
|                                                         | otherwise        |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``is_position(anything)``                               | returns ``True`` |
|                                                         | when passed a    |
|                                                         | valid Position   |
|                                                         | <h ttp://geojso  |
|                                                         | n.org/geojso     |
|                                                         | n-spec.html#     |
|                                                         | positions>\_ \_, |
|                                                         | otherwise        |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``is_point_coordinates(anything)``                      | \| returns       |
|                                                         | ``True`` when    |
|                                                         | passed valid     |
|                                                         | Point <http      |
|                                                         | ://geojson.o     |
|                                                         | rg/geojson-s     |
|                                                         | pec.html#poi     |
|                                                         | nt>\_\_          |
|                                                         | coordinates,     |
|                                                         | otherwise        |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``is_multi_point_coordinates(anything)``                |     returns      |
|                                                         |                  |
|                                                         | ``True`` when    |
|                                                         | passed valid     |
|                                                         | MultiPoint       |
|                                                         | <http://geoj     |
|                                                         | son.org/geoj     |
|                                                         | son-spec.htm     |
|                                                         | l#multipoint     |
|                                                         | >\_\_            |
|                                                         | coordinates,     |
|                                                         | otherwise        |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``is_line_string_coordinates(anything)``                |     returns      |
|                                                         |                  |
|                                                         | ``True`` when    |
|                                                         | passed valid     |
|                                                         | LineString       |
|                                                         | <http://geoj     |
|                                                         | son.org/geoj     |
|                                                         | son-spec.htm     |
|                                                         | l#linestring     |
|                                                         | >\_\_            |
|                                                         | coordinates,     |
|                                                         | otherwise        |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``is_linear_ring_coordinates(anything)``                |     returns      |
|                                                         |                  |
|                                                         | ``True`` when    |
|                                                         | passed valid     |
|                                                         | LinearRing       |
|                                                         | <http://geoj     |
|                                                         | son.org/geoj     |
|                                                         | son-spec.htm     |
|                                                         | l#linestring     |
|                                                         | >\_\_            |
|                                                         | coordinates,     |
|                                                         | otherwise        |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``is_multi_line_string_coordinates(anything)``          |     returns      |
|                                                         |                  |
|                                                         | ``True`` when    |
|                                                         | passed valid     |
|                                                         | MultiLineSt ring |
|                                                         | <http:/          |
|                                                         | /geojson.org     |
|                                                         | /geojson-spe     |
|                                                         | c.html#multi     |
|                                                         | linestring> \_\_ |
|                                                         | coordinates,     |
|                                                         | otherwise        |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``is_polygon_coordinates(anything)``                    | \| returns       |
|                                                         | ``True`` when    |
|                                                         | passed valid     |
|                                                         | Polygon <ht      |
|                                                         | tp://geojson     |
|                                                         | .org/geojson     |
|                                                         | -spec.html#p     |
|                                                         | olygon>\_\_      |
|                                                         | coordinates,     |
|                                                         | otherwise        |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``is_multi_polygon_coordinates(anything)``              |     returns      |
|                                                         |                  |
|                                                         | ``True`` when    |
|                                                         | passed valid     |
|                                                         | MultiPolygo n    |
|                                                         | <http://ge       |
|                                                         | ojson.org/ge     |
|                                                         | ojson-spec.h     |
|                                                         | tml#multipol     |
|                                                         | ygon>\_\_        |
|                                                         | coordinates,     |
|                                                         | otherwise        |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``is_point(anything)``                                  | returns ``True`` |
|                                                         | when passed a    |
|                                                         | valid Point      |
|                                                         | <http            |
|                                                         | ://geojson.o     |
|                                                         | rg/geojson-s     |
|                                                         | pec.html#poi     |
|                                                         | nt>\_\_,         |
|                                                         | otherwise        |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``is_multi_point(anything)``                            | \| returns       |
|                                                         | ``True`` when    |
|                                                         | passed a valid   |
|                                                         | MultiPoint       |
|                                                         | <http://geoj     |
|                                                         | son.org/geoj     |
|                                                         | son-spec.htm     |
|                                                         | l#multipoint     |
|                                                         | >\_\_, otherwise |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``is_line_string(anything)``                            | \| returns       |
|                                                         | ``True`` when    |
|                                                         | passed a valid   |
|                                                         | LineString       |
|                                                         | <http://geoj     |
|                                                         | son.org/geoj     |
|                                                         | son-spec.htm     |
|                                                         | l#linestring     |
|                                                         | >\_\_, otherwise |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``is_multi_line_string(anything)``                      |     returns      |
|                                                         |                  |
|                                                         | ``True`` when    |
|                                                         | passed a valid   |
|                                                         | MultiLineSt ring |
|                                                         | <http:/          |
|                                                         | /geojson.org     |
|                                                         | /geojson-spe     |
|                                                         | c.html#multi     |
|                                                         | linestring>      |
|                                                         | \_\_, otherwise  |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``is_polygon(anything)``                                | returns ``True`` |
|                                                         | when passed a    |
|                                                         | valid Polygon    |
|                                                         | <ht tp://geojson |
|                                                         | .org/geojson     |
|                                                         | -spec.html#p     |
|                                                         | olygon>\_\_,     |
|                                                         | otherwise        |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``is_multi_polygon(anything)``                          | \| returns       |
|                                                         | ``True`` when    |
|                                                         | passed a valid   |
|                                                         | MultiPolygo n    |
|                                                         | <http://ge       |
|                                                         | ojson.org/ge     |
|                                                         | ojson-spec.h     |
|                                                         | tml#multipol     |
|                                                         | ygon>\_\_,       |
|                                                         | otherwise        |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``is_geometry_collection(anything)``                    | \| returns       |
|                                                         | ``True`` when    |
|                                                         | passed a valid   |
|                                                         | GeometryCol      |
|                                                         | lection <htt     |
|                                                         | p://geojson.     |
|                                                         | org/geojson-spec |
|                                                         | .html#ge         |
|                                                         | ometry-colle     |
|                                                         | ction>\_\_,      |
|                                                         | otherwise        |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``is_feature(anything)``                                | returns ``True`` |
|                                                         | when passed a    |
|                                                         | valid Feature    |
|                                                         | <ht tp://geojson |
|                                                         | .org/geojson     |
|                                                         | -spec.html#f     |
|                                                         | eature-objec     |
|                                                         | ts>\_\_,         |
|                                                         | otherwise        |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``is_feature_collection(anything)``                     | \| returns       |
|                                                         | ``True`` when    |
|                                                         | passed a valid   |
|                                                         | Feature          |
|                                                         | Collection <     |
|                                                         | http://geojs     |
|                                                         | on.org/geojs     |
|                                                         | on-spec.html     |
|                                                         | #feature-col     |
|                                                         | lection-obje     |
|                                                         | cts>\_\_,        |
|                                                         | otherwise        |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``is_crs(anything)``                                    | returns ``True`` |
|                                                         | when passed a    |
|                                                         | valid CRS        |
|                                                         | <http:/          |
|                                                         | /geojson.org     |
|                                                         | /geojson-spe     |
|                                                         | c.html#coord     |
|                                                         | inate-refere     |
|                                                         | nce-system-o     |
|                                                         | bjects>\_\_,     |
|                                                         | otherwise        |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``has_crs(anything)``                                   | returns ``True`` |
|                                                         | when passed a    |
|                                                         | GeoJSON object   |
|                                                         | <http            |
|                                                         | ://geojson.o     |
|                                                         | rg/geojson-s     |
|                                                         | pec.html#geo     |
|                                                         | json-objects     |
|                                                         | >\_\_ that       |
|                                                         | validly          |
|                                                         | specifies a CRS  |
|                                                         | <http:/          |
|                                                         | /geojson.org     |
|                                                         | /geojson-spe     |
|                                                         | c.html#coord     |
|                                                         | inate-refere     |
|                                                         | nce-system-o     |
|                                                         | bjects>\_\_,     |
|                                                         | otherwise        |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``is_link(anything)``                                   | returns ``True`` |
|                                                         | when passed a    |
|                                                         | valid Link       |
|                                                         | <http:           |
|                                                         | //geojson.or     |
|                                                         | g/geojson-sp     |
|                                                         | ec.html#link     |
|                                                         | -objects>\_\_ ,  |
|                                                         | otherwise        |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``is_bbox(anything)``                                   | returns ``True`` |
|                                                         | when passed a    |
|                                                         | valid Bbox       |
|                                                         | <http:           |
|                                                         | //geojson.or     |
|                                                         | g/geojson-sp     |
|                                                         | ec.html#boun     |
|                                                         | ding-boxes>      |
|                                                         | \_\_, otherwise  |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``has_bbox(anything)``                                  | returns ``True`` |
|                                                         | when passed a    |
|                                                         | GeoJSON object   |
|                                                         | <http            |
|                                                         | ://geojson.o     |
|                                                         | rg/geojson-s     |
|                                                         | pec.html#geo     |
|                                                         | json-objects     |
|                                                         | >\_\_ that       |
|                                                         | validly          |
|                                                         | specifies a Bbox |
|                                                         | <http:           |
|                                                         | //geojson.or     |
|                                                         | g/geojson-sp     |
|                                                         | ec.html#boun     |
|                                                         | ding-boxes>      |
|                                                         | \_\_, otherwise  |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| ``equal_positions(position1, position2)``               | returns ``True`` |
|                                                         | when all         |
|                                                         | parameters are   |
|                                                         | identical        |
|                                                         | Positions <      |
|                                                         | http://geojs     |
|                                                         | on.org/geojs     |
|                                                         | on-spec.html     |
|                                                         | #positions>      |
|                                                         | \_\_, otherwise  |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+
| \`contained\_polygon(innerLinearRing, outerLinearRing)  | returns ``True`` |
| \`                                                      | when one         |
|                                                         | LinearRing       |
|                                                         | <http://geoj     |
|                                                         | son.org/geoj     |
|                                                         | son-spec.htm     |
|                                                         | l#linestring     |
|                                                         | >\_\_ contains   |
|                                                         | another,         |
|                                                         | otherwise        |
|                                                         | ``False``        |
+---------------------------------------------------------+------------------+

.. |Build Status| image:: https://img.shields.io/travis/dmtucker/gjtk-py.svg
   :target: https://travis-ci.org/dmtucker/gjtk-py
.. |PyPI Version| image:: https://img.shields.io/pypi/v/gjtk.svg
   :target: https://pypi.python.org/pypi/gjtk
