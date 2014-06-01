#!/usr/bin/env python

"""Show statistics on GeoJSON files."""

import argparse
import sys
from gjtk.process import *
from gjtk.validation import *


def survey_feature(feature):
    geometries = 0
    if is_geometry(feature['geometry']):
        geometries += survey_geometry(feature['geometry'])
    return geometries


def survey_geometry(geometry):
    geometries = 1
    if is_geometry_collection(geometry):
        for each in geometry:
            geometries += survey_geometry(each)
    return geometries


def main(files):
    valid = 0
    geometries = 0
    features = 0
    feature_collections = 0
    for opened in files:
        geojson = verify_geojson_file(opened)
        if geojson is False:
            continue
        valid += 1
        if is_feature_collection(geojson):
            feature_collections += 1
            for feature in geojson['features']:
                features += 1
                geometries += survey_feature(feature)
        elif is_feature(geojson):
            features += 1
            geometries += survey_feature(geojson)
        elif is_geometry(geojson):
            geometries += survey_geometry(geojson)
        else:
            raise RuntimeError('The GeoJSON validator has a bug!')
        opened.close()  # TODO
    print(str(valid) + '/' + str(len(files)) + ' valid GeoJSON files')
    print(str(feature_collections) + ' FeatureCollections')
    print(str(features) + ' Features')
    print(str(geometries) + ' Geometries')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'infile',
        help='',
        type=argparse.FileType('r'),
        default=[sys.stdin],
        nargs='*'
    )
    main(parser.parse_args().infile)
