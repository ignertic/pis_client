import setuptools
__version__="0.0.1"
with open("README.md", 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="pis_client",
    author="Gishobert Gwenzi",
    author_email="ilovebugsincode@gmail.com",
    version="0.0.1",
    description="Python PIS client",
    licence="MIT",
    long_description=long_description,
    url="http://github.com/ignertic/pis_client",
    packages=setuptools.find_packages(),
    install_requires=['loguru', 'requests'],
    entry_points={"console_scripts" : [""]},
    classifiers=[
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent"])
