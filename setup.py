#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-pendo2",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_pendo2"],
    install_requires=[
        # NB: Pin these to a more specific version for tap reliability
        "singer-python",
        "requests",
    ],
    entry_points="""
    [console_scripts]
    tap-pendo2=tap_pendo2:main
    """,
    packages=["tap_pendo2"],
    package_data = {
        "schemas": ["tap_pendo2/schemas/*.json"]
    },
    include_package_data=True,
)
