#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

version = '0.1.1'
long_description = '\n'.join([
    open('README.rst').read(),
    open('AUTHORS.rst').read(),
    open('HISTORY.rst').read(),
    ])

classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Plugins',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name='pygments-style-solarized',
    version=version,
    description='Pygments version of the Solarized theme.',
    long_description=long_description,
    classifiers=classifiers,
    keywords=['pygments', 'style', 'solarized', 'syntax highlighting'],
    author='Shoji KUMAGAI',
    author_email='take dot this dot 2 dot your dot grave at gmail dot com',
    url='https://github.com/shkumagai/pygments-style-solarized',
    license='MIT',
    packages=find_packages(),
    install_requires=['pygments >= 1.5'],
    entry_points="""
        [pygments.styles]
        solarized-light=pygments_style_solarized.light:LightStyle
        solarized-dark=pygments_style_solarized.dark:DarkStyle
    """,
    zip_safe=False,
)
