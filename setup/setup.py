from setuptools import setup, find_packages

with open("README.md", "r") as file:
	long_description = file.read()

link = 'https://github.com/xXxCLOTIxXx/nz-ua.py/archive/refs/heads/main.zip'
ver = '1.1.5'

setup(
	name = "nz-ua.py",
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
		"async"
		"api",
		"python",
		"python3",
		"python3.x",
		"xsarz",
		"official"
	],
	install_requires = [
		"colored",
		"aiohttp",
		"requests",
		"aiofiles"
	],
	packages = find_packages()
)
