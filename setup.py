from setuptools import setup, find_packages


def get_description():
    with open("README.md") as file:
        return file.read()


def get_requirements():
    with open("requirements.txt") as file:
        return file.read().splitlines()


setup(
    name="nz-ua",
    url="https://github.com/GoldMasterPro/nz-ua",
    version="2.0.0",
    author="GoldMasterPro",
    description="Library for working with the nz.ua service",
    license="MIT",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    long_description=get_description(),
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
