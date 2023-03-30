from setuptools import setup, find_packages
import re


def _get_variable_from_init_file(variable_name: str) -> str:
    with open('nz/__init__.py') as file:
        pattern: str = rf"^{variable_name}\s*=\s*[\'\"]([^\'\"]*)[\'\"]"
        return re.search(pattern, file.read(), re.MULTILINE).group(1)


def get_long_description() -> str:
    with open("README.md") as file:
        return file.read()


def get_requirements() -> list:
    with open("requirements.txt") as file:
        return file.read().splitlines()


NAME = _get_variable_from_init_file("__title__")
VERSION = _get_variable_from_init_file("__version__")
AUTHOR = _get_variable_from_init_file("__author__")
DESCRIPTION = _get_variable_from_init_file("__description__")
LONG_DESCRIPTION = get_long_description()
REQUIREMENTS = get_requirements()

setup(
    name=NAME,
    url="https://github.com/GoldMasterPro/nz-ua",
    project_urls={
        'Documentation': 'https://GoldMasterPro.github.io/nz-ua',
    },
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    license="MIT",
    packages=find_packages(),
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    install_requires=REQUIREMENTS,
    python_requires='>=3.10.0',
    keywords=[
        "nz",
        "nz-ua",
        "nz.ua",
        "async",
        "api",
        "python",
        "python3",
        "python3.11",
    ],
)
