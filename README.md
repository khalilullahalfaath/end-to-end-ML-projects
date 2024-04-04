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

> Note that each folder must have an __init__.py file so it can be detected as a package in this setup file.

#### Create requirements.txt

requirements.txt include all of the library needed to run the project. It ends with ``-e .`` to automatically trigger the setup.py to download and install those packages.

### 2. Create project /src and __init__.py file

### 3. Create project structures

The project's source code resides in the ```src``` directory. This directory is organized with key folders for specific functionalities to make the code clean.

<!-- markdownlint-disable code-block-style -->
```markdown
.
├── ... 
├── src  
│   ├── components  # Reusable modules for data handling and model building
│   │   ├── __init__.py  # Initialization file (optional, can be empty)
│   │   ├── data_ingestion.py  # Functions for data acquisition and preprocessing
│   │   ├── data_transformation.py  # Functions for feature engineering and data preparation
│   │   ├── model_training.py  # Functions for training and evaluating machine learning models
│   │   ├── pipeline  # Pre-defined pipelines for common workflows
│   │   │   ├── __init__.py  # Initialization file (optional, can be empty)
│   │   │   ├── predict_pipeline.py  # Functions for creating and executing prediction pipelines
│   │   │   └── train_pipeline.py  # Functions for creating and executing training pipelines
│   │   ├── __init__.py  # Initialization file (optional, can be empty)
│   │   ├── exception.py  # Custom exceptions for project-specific machine learning errors
│   │   ├── logger.py  # Functions for structured logging during training, evaluation, and deployment
│   │   └── utils.py  # Helper functions for common tasks (e.g., data validation, file I/O)
├── venv  # Virtual environment directory (if using virtual environments)
├── .gitignore  # File specifying files/patterns to exclude from Git version control
├── README.md  # Project documentation (purpose, usage instructions, dependencies)
├── requirements.txt  # Text file listing project dependencies for easy installation
└── setup.py  # Script for packaging and distributing the project
```

Description:

- __src__ directory: Houses the core, well-structured source code for the machine learning project.
- __components__ subdirectory: Contains reusable Python modules for various aspects of the machine learning workflow.
- `__init__.py` files (optional): Can be used to establish these directories as Python packages, allowing for organized imports.
- __data_ingestion.py__: Defines functions for acquiring data from various sources and performing any necessary preprocessing steps.
- __data_transformation.py__: Implements methods for feature engineering and data preparation, ensuring data is suitable for machine learning algorithms.
- __model_training.py__: Encapsulates functions for training and evaluating various machine learning models. Includes mechanisms for data loading, splitting, training, and performance assessment.
- __pipeline__ subdirectory (optional): Houses pre-defined pipelines for common machine learning workflows (e.g., training, prediction) to promote code efficiency and maintainability.
  - `predict_pipeline.py`: Encapsulates the logic for creating and executing prediction pipelines, enabling inference on new data.
  - `train_pipeline.py`: Defines functions for creating and executing training pipelines, encompassing data loading, training, evaluation, and potentially model saving.
- __exception.py__: Defines custom exceptions specifically related to the project's machine learning operations for more informative error handling.
- __logger.py__: Provides structured logging functionalities during training, evaluation, and deployment, allowing for debugging, monitoring, and analysis.
- __utils.py__: Contains helper functions for common tasks across different parts of the project, promoting code reusability.
- __venv__ directory: If using virtual environments for dependency management, this directory would contain the isolated environment for the project.
- __.gitignore__ file: Specifies files or patterns to be excluded from version control using Git, keeping the repository clean and avoiding unnecessary commits for files like configuration settings or temporary data.
- __README.md__ file: Provides essential documentation for the project, including its purpose, usage instructions, dependencies, and any relevant setup steps.
- __requirements.txt__ file: Lists the project's external dependencies, enabling easy installation and replication of the project's environment.
- __setup.py__ file (optional): If the project is intended for distribution or reusability, this script can be used to package it as a Python library.
<!-- markdownlint-restore -->