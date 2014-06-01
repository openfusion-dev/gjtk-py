#!/usr/bin/env python

"""Validate GeoJSON files."""

import argparse
import sys
from gjtk.process import *


def main(files):
    valid = 0
    for opened in files:
        sys.stdout.write(opened.name+'... ')
        if verify_geojson_file(opened):
            valid += 1
            print('valid')
        else:
            print('invalid')
        if opened.close():  # TODO
            print 'successful close'
        else:
            print 'failed close'
    print(str(valid) + '/' + str(len(files)) + ' valid GeoJSON files')


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
