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
    author_email='dmtucker@ucsc.edu',
    license='LGPLv2+',
    url='https://github.com/openfusion-dev/gjtk-py',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>= 3.5',
    install_requires=[
        'decorator ~= 4.0',
        'matplotlib ~= 1.5',
        'attrs < 19.2.0',  # https://github.com/pytest-dev/pytest/issues/3223
        'pytest ~= 3.3.1',
    ],
    entry_points={'console_scripts': ['gjtk = gjtk.cli:main']},
    keywords='GeoJSON',
    classifiers=[
        'License :: OSI Approved :: '
        'GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Development Status :: 5 - Production/Stable',
    ],
)
