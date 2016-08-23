# coding: utf-8

"""This module defines the GJTK CLI."""

from __future__ import absolute_import
from __future__ import print_function

from io import open  # pylint: disable=redefined-builtin

import argparse
import json
import sys

import gjtk.validate


def parser(argument_parser=None):
    """Define a CLI."""
    if argument_parser is None:
        argument_parser = argparse.ArgumentParser(prog="gjtk")
    argument_parser.add_argument(
        "paths", nargs='+', metavar="path",
        help="Specify GeoJSON files to validate.",
    )
    return argument_parser


def main(argv=None):
    """Execute CLI invocations."""

    if argv is None:
        argv = sys.argv[1:]
    args = parser().parse_args(argv)

    valid_paths = 0
    len_longest_path = max(map(len, args.paths))
    for path in args.paths:
        pad = ' ' * (len_longest_path - len(path))
        print(path + pad, end='\t')
        try:
            with open(path, 'r', encoding='utf-8') as f:
                valid_json = json.load(f)
        except IOError as ex:
            print('error', ex)
            continue
        except ValueError:
            print('invalid JSON')
            continue
        if gjtk.validate.is_geojson(valid_json):
            print('valid')
            valid_paths += 1
        else:
            print('invalid')
    print(str(valid_paths) + '/' + str(len(args.paths)), 'valid GeoJSON files')

    sys.exit(len(args.paths) - valid_paths)
