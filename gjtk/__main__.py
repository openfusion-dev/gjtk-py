

import json
import gjtk


def load_geojson_file(*args):
    """Load and validate GeoJSON files."""
    for arg in args:
        with open(arg) as data:
            verify_geojson_file(data)


def print_geojson(geojson, indent=4, separators=(",", ": ")):
    """Print a GeoJSON object."""
    print json.dumps(geojson, indent=indent, separators=separators)


def verify_geojson_file(*args):
    """Parse and validate opened GeoJSON files."""
    for arg in args:
        try:
            loaded = json.load(arg)
        except ValueError as error:
            print error
            return False
        if gjtk.isGeoJSON(loaded):
            return loaded
        else:
            return False

