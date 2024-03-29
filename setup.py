#!/usr/bin/env python
from setuptools import setup, find_packages

requires = ['Sphinx>=0.6',
        ]

setup(
    name='sphinxcontrib-plot',
    version='1.1.3',
    url='https://github.com/stathissideris/sphinxcontrib-plot',
    license='GPLv3',
    author='Yongping Guo',
    author_email='guoyoooping@163.com',
    description='Embed gnuplot, ditaa, pyplot, DOT, etc. diagrams in your Sphinx-based documentation.',
    long_description=open('README.rst').read(),
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
