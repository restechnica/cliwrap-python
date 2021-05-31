#!/usr/bin/env python3

import os
from setuptools import setup, find_packages

version = os.getenv('RELEASE_VERSION', '0.0.0')


def long_description():
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()


setup(
    name='cliwrap',
    description='A lightweight wrapper around CLIs for error handling and logging.',
    license="Mozilla Public License Version 2.0",
    long_description=long_description(),
    packages=find_packages(),
    python_requires=">=3.6",
    url='https://github.com/restechnica/cliwrap-python',
    version=version
)
