from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in xpert_hr/__init__.py
from xpert_hr import __version__ as version

setup(
	name="xpert_hr",
	version=version,
	description="New features for stock and HR modules",
	author="MicroMerger",
	author_email="m.gulzar@pk.micromerger.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
