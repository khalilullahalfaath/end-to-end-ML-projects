from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(path: str) -> List[str]:
    """
    this function will return the list of strings contain the requirement needed
    """
    requirements = []
    with open(path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="end-to-end ml project",
    version="0.0.1",
    author="Aleeel",
    author_email="khalilullah.alfaath21@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
