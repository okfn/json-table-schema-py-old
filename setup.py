#!/usr/bin/env python

from setuptools import setup

import io
import os

DIR = os.path.abspath(os.path.dirname(__file__))
README = 'README.md'
README_PATH = os.path.join(DIR, README)

print("json-table-schema has been replaced by jsontableschema. "
      "See https://github.com/okfn/json-table-schema-py-old for details.")


with io.open(README_PATH, mode='r+t', encoding='utf-8') as stream:
    description_text = stream.read()

setup(
    name="json-table-schema",
    author="Open Knowledge",
    author_email="info@okfn.org",
    url="https://github.com/okfn/json-table-schema-py-old",
    version="0.5.0",
    description="Python library for dealing with JSON Table Schema files",
    long_description=description_text,
    install_requires=['jsontableschema>=0.5.1'],
    classifiers=['Development Status :: 7 - Inactive']
)
