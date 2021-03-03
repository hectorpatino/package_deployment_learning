# Packages for python guidelines

This document was created following the [Python: Coding Guideline, Tooling, Unit Testing and Packages
in Udemy](https://www.udemy.com/course/python-coding-guidelines-tooling-testing-and-packaging)

# Configuration

on ```requirements-dev.txt```
```
--requirement requiremets.txt
```

## Linting

```cmd
pip install pylint
pip install flake8
pip install mypy
pip install autopep8
pip install isort
pip install pydocstyle
pip install black
```

## Documentation
```cmd
pip install mkdocs
pip install mkdocstrings
pip install mkdocs-material
pip install Pygments
```

## Testing
```cmd
pip install pytest
pip install codecov
pip install pytest-cov
pip install tox
pip install pre-commit
pip install pytest-benchmark
```

# Guidelines and Docstring

## [Pylint](http://pylint.pycqa.org/en/latest/)

This helps to check PEP8

To check
```cmd
pylint filename.py
```

For configurations I can modify the next text file using the code of the warning,
that warning is usually like ```regex ^.*?\([A-z]+\-[A-z]\)$```

```cmd
pylint --generate-rcfile > .pylintrc
```

for help
```cmd
pylint --help-msg=missing-module-docstring
```

## [Flake8](https://flake8.pycqa.org/en/latest/#)
A better, faster way to check pep8. its faster because pylint goes in deep
It install pycodesyle, pyflaakes, and mccabe

```cmd
python -m pip install flake8
```

To use
```cmd
flake8 path/to/code/to/check.py
# or
flake8 path/to/code/
```

## [isort](https://pycqa.github.io/isort/)
[Github](https://github.com/PyCQA/isort)

alphabetically sort imports.

```cmd
isort mypythonfile.py mypythonfile2.py
```
For configuration it support setup.cfg, tox.ini or .flake8 files, [this](https://flake8.pycqa.org/en/latest/user/configuration.html)
link will guide the process and creation of .flakefile

For [configuration](https://pycqa.github.io/isort/docs/configuration/config_files/) isort supports various files
.isort.cfg, pyproject.toml, setup.cfg, tox.ini and .editorconfig

## [autopep8](https://github.com/hhatto/autopep8/actions)

It is a formater it would modify the code.

To use with aggressive level 2
```cmd
autopep8 --in-place --aggressive --aggressive <filename>
```

it uses flake 8 config files

## [Black](https://black.readthedocs.io/en/stable/?badge=stable)
[Github](https://github.com/psf/black)

# Documentation
## [Google](https://google.github.io/styleguide/pyguide.html#s3.8.1-comments-in-doc-strings)
[An example](https://gist.github.com/redlotus/3bc387c2591e3e908c9b63b97b11d24e)

```python
def function_with_types_in_docstring(param1, param2):
    """Example function with types documented in the docstring.
    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:
    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.
    Returns:
        bool: The return value. True for success, False otherwise.
    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.
    """
```

## [pydocstyle](http://www.pydocstyle.org/en/stable/)
Usage

```cmd
pydocstyle  --convention=google python_file.py
```

Configuration
pydocstyle supports ini-like configuration files. In order for pydocstyle
to use it, it must be named one of the following options, and have a pydocstyle section.
its goot to use .pydocstyle
## [Creation](https://www.mkdocs.org/)

Create _mkdocs.yml_, _docs.index.md_
on
```
mkdocs.yml
```
```yml
site_name: My Package
site_description: "Some description."

theme:
  name: "readthedocs"

plugins:
  - search
  - mkdocstrings

markdown_extensions:
  - pymdownx.highlight
  - pymdownx.superfences

nav:
  - "Start": index.md
  - "API": api.md
  - "XXX": xxx.md

```

on ```api.md```
```md
# References

## Chair

::: chairs.chair
```

to build

```cmd
build
```
To visualize it
```cmd
mkdocs serve
```

To publish in Github
```cmd
git push origin main
mkdocs gh-deploy
```

## [Type Annotations](https://docs.python.org/3/library/typing.html) and [Mypy](https://mypy.readthedocs.io/en/stable/)
For functions that just checks types a good practice may be NoReturn.


```cmd
mypy program.py
```
For mypy configuration .mypy.ini

It is posible to create a single file with all configurations the file should be named __setup.cfg__.

# Testing
To veryfy the coverage of testing, important pytest and codecov

 ```cmd
pytest --cov package_name tests_folder
```
To visualize it on html
```cmd
pytest --cov package_name test_folder --cov-report=html
```
Then open ```htmlcov/index.html```


# Packaging

On init.py
```python
from .class import Class
____all____ = ['Class']
```
## [setup.py](https://packaging.python.org/tutorials/packaging-projects/)
create setup.py
```
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-YOUR-USERNAME-HERE", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires = ["numpy"]
)
```




on ```README.md```
```md
# Example Package

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.
```

### Using Twine
the next code is for testpypi

```cmd
python3 -m pip install --upgrade build
python3 -m build
python3 -m pip install --user --upgrade twine
python3 -m twine upload --repository testpypi dist/*
```
#### Using API-TOKEN
for usint [link](https://docs.travis-ci.com/user/deployment/pypi/)

### Install
install a reference.
```cmd
python setup.py develop
```

install into enviroment
```cmd
python setup.py install
```

__NOTE__: Requirements is used for github, Install requires on ```setup.py``` for PyPÏ

### Makefile
its a good way to run commands an be lazy.


# Github Workflows and Pre-Commits

## [Precommit](https://pre-commit.com/)
Useful for the coding style of the package. the setup files is ```.pre-commit-config.yaml```

cuando un error falla el intenara corregirlo
```cmd
pre-commit install
pre-commit run --all-files
```

## [github actions](https://docs.github.com/en/actions/guides/building-and-testing-python)

create ```.github/workflows```
