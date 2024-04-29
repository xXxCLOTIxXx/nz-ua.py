from setuptools import setup, find_packages

with open("README.md", "r") as file:
	long_description = file.read()

link = 'https://github.com/xXxCLOTIxXx/nz-ua.py/archive/refs/heads/main.zip'
ver = '1.1.6'

setup(
	name = "nz",
	version = ver,
	url = "https://github.com/xXxCLOTIxXx/nz-ua.py",
	download_url = link,
	license = "MIT",
	author = "Xsarz",
	author_email = "xsarzy@gmail.com",
	description = "Library for working with the nz-ua application.",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	keywords = [
		"nz",
		"nz.py",
		"nz-ua",
		"nz-ua.py",
		"nz.ua",
		"async"
		"api",
		"python",
		"python3",
		"python3.x",
		"xsarz",
		"official"
	],
	install_requires = [
		"aiohttp"
	],
	packages = find_packages()
)
