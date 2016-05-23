#!/usr/bin/env python
# coding: utf-8

"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    README = readme_file.read()

setup(
    name='gjtk',
    version='3.0.0',
    description='GeoJSON ToolKit',
    long_description=README,
    author='David Tucker',
    author_email='david.michael.tucker@gmail.com',
    license='LGPLv2+',
    url='https://github.com/dmtucker/gjtk-py',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data=True,
    test_suite="gjtk.test",
    install_requires=['matplotlib'],
    entry_points={'console_scripts': ['gjtk = gjtk.__main__:main']},
    keywords='GeoJSON',
    classifiers=[
        'License :: OSI Approved :: '
        'GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
        'Development Status :: 4 - Beta',
    ],
)
