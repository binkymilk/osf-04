# -*- coding: utf-8 -*-

# Import modules
from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="geogra.py",
    version="1.0.0",
    author="Bianca Silmaro",
    author_email="bianca@thinkingmachin.es",
    install_requires=requirements,
    scripts=["geogra.py"]
)
