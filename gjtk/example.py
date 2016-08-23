# coding: utf-8

"""GeoJSON Examples from the Specification"""

POINT = {
    "type": "Point",
    "coordinates": [100.0, 0.0],
}

MULTI_POINT = {
    "type": "MultiPoint",
    "coordinates": [[100.0, 0.0], [101.0, 1.0]],
}

LINE_STRING = {
    "type": "LineString",
    "coordinates": [[100.0, 0.0], [101.0, 1.0]],
}

MULTI_LINE_STRING = {
    "type": "MultiLineString",
    "coordinates": [
        [[100.0, 0.0], [101.0, 1.0]],
        [[102.0, 2.0], [103.0, 3.0]],
    ],
}

POLYGON_WITHOUT_HOLE = {
    "type": "Polygon",
    "coordinates": [
        [[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]],
    ],
}

POLYGON_WITH_HOLE = {
    "type": "Polygon",
    "coordinates": [
        [[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]],
        [[100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8], [100.2, 0.2]],
    ],
}

MULTI_POLYGON = {
    "type": "MultiPolygon",
    "coordinates": [
        [
            [[102.0, 2.0], [103.0, 2.0], [103.0, 3.0], [102.0, 3.0], [102.0, 2.0]],
        ],
        [
            [[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]],
            [[100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8], [100.2, 0.2]],
        ],
    ],
}

GEOMETRY_COLLECTION = {
    "type": "GeometryCollection",
    "geometries": [
        {
            "type": "Point",
            "coordinates": [100.0, 0.0],
        },
        {
            "type": "LineString",
            "coordinates": [[101.0, 0.0], [102.0, 1.0]],
        },
    ],
}

FEATURE = {
    "type": "Feature",
    "geometry": {
        "type": "Point",
        "coordinates": [125.6, 10.1],
    },
    "properties": {
        "name": "Dinagat Islands",
    },
}

FEATURE_COLLECTION = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [102.0, 0.5]},
            "properties": {"prop0": "value0"},
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [102.0, 0.0],
                    [103.0, 1.0],
                    [104.0, 0.0],
                    [105.0, 1.0],
                ],
            },
            "properties": {
                "prop0": "value0",
                "prop1": 0.0,
            },
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [100.0, 0.0],
                        [101.0, 0.0],
                        [101.0, 1.0],
                        [100.0, 1.0],
                        [100.0, 0.0],
                    ],
                ],
            },
            "properties": {
                "prop0": "value0",
                "prop1": {"this": "that"},
            },
        },
    ],
}

CRS_1 = {
    "type": "name",
    "properties": {
        "name": "urn:ogc:def:crs:OGC:1.3:CRS84",
    },
}

CRS_2 = {
    "type": "link",
    "properties": {
        "href": "http://example.com/crs/42",
        "type": "proj4",
    },
}

CRS_3 = {
    "type": "link",
    "properties": {
        "href": "data.crs",
        "type": "ogcwkt",
    },
}

LINK_1 = {
    "href": "http://example.com/crs/42",
    "type": "proj4",
}

LINK_2 = {
    "href": "data.crs",
    "type": "ogcwkt",
}

BBOX_1 = [-10.0, -10.0, 10.0, 10.0]

BBOX_2 = [100.0, 0.0, 105.0, 1.0]
