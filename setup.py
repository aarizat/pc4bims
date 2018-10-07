#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

setup(
    author="Andres Ariza-Triana & Ludger O. Suarez-Burgoa",
    author_email='aarizatr@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    description="Circle packing in arbitrary polygns.",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    keywords='pc4bims',
    name='pc4bims',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    url='https://github.com/aarizat/pc4bims',
    version='0.1.0',
    zip_safe=False,
)
