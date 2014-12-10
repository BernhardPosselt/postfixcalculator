#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='postfixcalculator',
    version='0.1',
    description='Postfix calculator',
    author='Bernhard Posselt',
    author_email='dev@bernhard-posselt.com',
    packages=find_packages(exclude=['tests*']),
    install_requires=[],
    test_suite='tests',
)