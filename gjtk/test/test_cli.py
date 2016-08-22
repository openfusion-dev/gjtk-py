# coding: utf-8

"""Tests for gjtk.cli"""

from __future__ import absolute_import

import os

import decorator

import gjtk.cli


def exit_with_status(comp=None):
    """
    Expect a test to raise a SystemExit, optionally with a code that satisfies the given expression.
    """
    def _decorator(test_func):
        """Decorate tests."""
        def _decorated(test_func, *args, **kwargs):
            """A replacement test function that expects tests to raise SystemError."""
            try:
                assert test_func(*args, **kwargs) and False
            except SystemExit as exc:
                expr = str(exc.code) + ' ' + comp
                assert True if comp is None else eval(expr), expr  # pylint: disable=eval-used
        return decorator.decorator(_decorated, test_func)
    return _decorator


@exit_with_status('!= 0')
def test___main__():
    """Test python -m functionality."""
    import gjtk.__main__  # pylint: disable=redefined-outer-name, unused-variable


@exit_with_status('!= 0')
def test_empty():
    """Test invocation with no arguments."""
    gjtk.cli.main()


@exit_with_status('!= 0')
def test_nonexistent_file(tmpdir):
    """Test invocation with a file that does not exist."""
    gjtk.cli.main(argv=[os.path.join(str(tmpdir), 'x')])


@exit_with_status('!= 0')
def test_non_file(tmpdir):
    """Test invocation with a directory."""
    gjtk.cli.main(argv=[str(tmpdir)])


@exit_with_status('!= 0')
def test_incorrect_encoding(non_utf8_file):
    """Test invocation with a non-UTF-8 file."""
    gjtk.cli.main(argv=[non_utf8_file])


@exit_with_status('!= 0')
def test_empty_file(tmpdir):
    """Test invocation with an empty file."""
    gjtk.cli.main(argv=[str(tmpdir.join('empty'))])


@exit_with_status('!= 0')
def test_non_json_file(text_file):
    """Test invocation with a file that does not contain JSON."""
    gjtk.cli.main(argv=[text_file])


@exit_with_status('!= 0')
def test_invalid_file(json_file):
    """Test invocation with a valid JSON file that is not GeoJSON."""
    gjtk.cli.main(argv=[json_file])


@exit_with_status('== 0')
def test_valid_file(geojson_file):
    """Test invocation with a valid GeoJSON file."""
    gjtk.cli.main(argv=[geojson_file])


@exit_with_status('== 1')
def test_mixed_files(geojson_file, json_file):
    """Test invocation with a valid GeoJSON file and an invalid one."""
    gjtk.cli.main(argv=[geojson_file, json_file])
