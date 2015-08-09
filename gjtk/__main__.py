

import argparse
import json
import sys

import gjtk


def load_geojson_file(*args):  # TODO
    """Load and validate GeoJSON files."""
    for arg in args:
        with open(arg) as data:
            verify_geojson_file(data)


def print_geojson(geojson, indent=4, separators=(",", ": ")):  # TODO
    """Print a GeoJSON object."""
    print json.dumps(geojson, indent=indent, separators=separators)







def lint(args):
    valid = 0
    for path in args.paths:
        with open(path, 'r') as f:
            anything = json.load(f)
        sys.stdout.write(path+'... ')
        if gjtk.validate.isGeoJSON(anything):
            valid += 1
            print('valid')
        else:
            print('invalid')
    print(str(valid) + '/' + str(len(args.paths)) + ' valid GeoJSON files')


def stat(args):
    valid = 0
    geometries = 0
    features = 0
    feature_collections = 0
    for path in args.paths:
        with open(path, 'r') as f:
            geojson = json.load(f)
        if not gjtk.validate.isGeoJSON(geojson):
            continue
        valid += 1
        if gjtk.validate.isFeatureCollection(geojson):
            feature_collections += 1
            for feature in geojson['features']:
                features += 1
                geometries += stat_feature(feature)
        elif gjtk.validate.isFeature(geojson):
            features += 1
            geometries += stat_feature(geojson)
        else:
            assert gjtk.validate.isGeometry(geojson), 'A valid GeoJSON object is not a FeatureCollection, Feature, or Geometry!\n{0}'.format(gjtk.test.error_message(test_data=geojson))
            geometries += stat_geometry(geojson)
    print(str(valid) + '/' + str(len(args.paths)) + ' valid GeoJSON files')
    print(str(feature_collections) + ' FeatureCollections')
    print(str(features) + ' Features')
    print(str(geometries) + ' Geometries')


def stat_feature(feature):
    geometries = 0
    if gjtk.validate.isGeometry(feature['geometry']):
        geometries += stat_geometry(feature['geometry'])
    return geometries


def stat_geometry(geometry):
    geometries = 1
    if gjtk.validate.isGeometryCollection(geometry):
        for each in geometry['geometries']:
            geometries += stat_geometry(each)
    return geometries


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="gjtk")
    subparsers = parser.add_subparsers()
    
    lint_parser = subparsers.add_parser(
        "lint",
        help="Validate a GeoJSON file."
    )
    lint_parser.add_argument(
        "paths", nargs='+', metavar="path",
        help="Specify GeoJSON file(s)."
    )
    lint_parser.set_defaults(func=lint)
    
    stat_parser = subparsers.add_parser(
        "stat",
        help="Show information about a GeoJSON file."
    )
    stat_parser.add_argument(
        "paths", nargs='+', metavar="path",
        help="Specify GeoJSON file(s)."
    )
    stat_parser.set_defaults(func=stat)

    args = parser.parse_args()
    args.func(args)

