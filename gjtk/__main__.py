"""GJTK Default Interface"""

from __future__ import absolute_import
from __future__ import print_function

import argparse
import json
import sys

import gjtk


def lint(args):
    """Validate GeoJSON files."""
    valid = 0
    len_longest_path = max(map(len, args.paths))
    for path in args.paths:
        pad = ' ' * (len_longest_path - len(path))
        print(path + pad, end='\t')
        try:
            with open(path, 'r') as f:
                try:
                    anything = json.load(f)
                except json.decoder.JSONDecodeError:
                    print('invalid')
                    continue
        except IOError as ex:
            print('error', ex)
            continue
        if gjtk.validate.is_geojson(anything):
            valid += 1
            print('valid')
        else:
            print('invalid')
    print(str(valid) + '/' + str(len(args.paths)), 'valid GeoJSON files')
    return len(args.paths) - valid


def stat(args):
    """Count the number of GeoJSON objects present of each type."""
    valid = 0
    geometries = 0
    features = 0
    feature_collections = 0
    for path in args.paths:
        with open(path, 'r') as f:
            geojson = json.load(f)
        if not gjtk.validate.is_geojson(geojson):
            continue
        valid += 1
        if gjtk.validate.is_feature_collection(geojson):
            feature_collections += 1
            for feature in geojson['features']:
                features += 1
                geometries += stat_feature(feature)
        elif gjtk.validate.is_feature(geojson):
            features += 1
            geometries += stat_feature(geojson)
        else:
            assert gjtk.validate.is_geometry(geojson)
            geometries += stat_geometry(geojson)
    print(str(valid) + '/' + str(len(args.paths)) + ' valid GeoJSON files')
    print(str(feature_collections) + ' FeatureCollections')
    print(str(features) + ' Features')
    print(str(geometries) + ' Geometries')


def stat_feature(feature):
    """Count the number of Geometries in a Feature."""
    geometries = 0
    if gjtk.validate.is_geometry(feature['geometry']):
        geometries += stat_geometry(feature['geometry'])
    return geometries


def stat_geometry(geometry):
    """Count the number of Geometries in a Geometry."""
    geometries = 1
    if gjtk.validate.is_geometry_collection(geometry):
        for each in geometry['geometries']:
            geometries += stat_geometry(each)
    return geometries


def main():
    """Parse an execute the CLI."""
    parser = argparse.ArgumentParser(prog="gjtk")
    subparsers = parser.add_subparsers()

    lint_parser = subparsers.add_parser(
        "lint",
        help="Validate a GeoJSON file.",
    )
    lint_parser.add_argument(
        "paths", nargs='+', metavar="path",
        help="Specify GeoJSON file(s).",
    )
    lint_parser.set_defaults(func=lint)

    stat_parser = subparsers.add_parser(
        "stat",
        help="Show information about a GeoJSON file.",
    )
    stat_parser.add_argument(
        "paths", nargs='+', metavar="path",
        help="Specify GeoJSON file(s).",
    )
    stat_parser.set_defaults(func=stat)

    args = parser.parse_args()
    return args.func(args)


if __name__ == '__main__':
    sys.exit(main())
