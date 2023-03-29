from setuptools import setup, find_packages
import re


def _get_variable_from_init_file(variable_name: str) -> str:
    with open('nz/__init__.py') as file:
        pattern: str = rf"^{variable_name}\s*=\s*[\'\"]([^\'\"]*)[\'\"]"
        return re.search(pattern, file.read(), re.MULTILINE).group(1)


def get_version():
    return _get_variable_from_init_file("__version__")


def get_name():
    return _get_variable_from_init_file("__title__")


def get_author():
    return _get_variable_from_init_file("__author__")


def get_license():
    return _get_variable_from_init_file("__license__")


def get_description():
    return _get_variable_from_init_file("__description__")


def get_long_description():
    with open("README.md") as file:
        return file.read()


def get_requirements():
    with open("requirements.txt") as file:
        return file.read().splitlines()


setup(
    name=get_name(),
    url="https://github.com/GoldMasterPro/nz-ua",
    project_urls={
        'Documentation': 'https://GoldMasterPro.github.io/nz-ua',
    },
    version=get_version(),
    author=get_author(),
    description=get_description(),
    license=get_license(),
    packages=find_packages(),
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    install_requires=get_requirements(),
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
