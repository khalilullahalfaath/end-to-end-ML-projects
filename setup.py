from setuptools import find_packages, setup
from typing import List

setup(
    name="end-to-end ml project",
    version="0.0.1",
    author="Aleeel",
    author_email="khalilullah.alfaath21@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
