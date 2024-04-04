# End-to-end Machine Learning Projects Codebase

This repository will be customized for my upcoming data science projects based on [this tutorial](https://www.youtube.com/watch?v=Rv6UFGNmNZg&list=PLZoTAELRMXVPS-dOaVbAux22vzqdgoGhG&index=2&pp=iAQB). I am using this tutorial to learn how ML projects were used in production.

---

## Steps

### 1. Set up the github repository

#### Create a new environment

```bash
conda create -p {environment_name} python=={python_version} -y
```

```bash
conda activate venv/
```

#### Create setup.py

See this [docs](https://docs.python.org/3.11/distutils/setupscript.html). Setup.py is basically used to build the entire projects as a package.

```python
setup(
    name="end-to-end ml project",
    version="0.0.1",
    author="Aleeel",
    author_email="khalilullah.alfaath21@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
# find_packages() will return all of the requirements needed. Above that define the function to get requirements from requirements.txt
```

> Note that ach folder must have an __init__.py file so it can be detected as a package in this setup file.

#### Create requirements.txt

requirements.txt include all of the library needed to run the project. It ends with ``-e .`` to automatically trigger the setup.py to download and install those packages.


### 2. 