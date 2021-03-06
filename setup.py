"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages  # type: ignore

with open('README.rst') as readme_file:
    README = readme_file.read()

setup(
    name='gjtk',
    use_scm_version=True,
    description='GeoJSON ToolKit',
    long_description=README,
    author='David Tucker',
    author_email='dmtucker@ucsc.edu',
    license='LGPLv2+',
    url='https://github.com/openfusion-dev/gjtk-py',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    python_requires='>= 3.5',
    setup_requires=[
        'setuptools-scm >= 3.3',
    ],
    install_requires=[
        'decorator >= 4.0',
        'matplotlib >= 1.5',
    ],
    entry_points={'console_scripts': ['gjtk = gjtk.cli:main']},
    keywords='GeoJSON',
    classifiers=[
        'License :: OSI Approved :: '
        'GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Development Status :: 5 - Production/Stable',
    ],
)
