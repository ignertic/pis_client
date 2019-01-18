import setuptools

with open("README.md", 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybluedot",
    author="Gishobert Gwenzi",
    author_email="ilovebugsincode",
    version="0.0.5",
    description="BluedotSMS python wrapper",
    long_description=long_description,
    url="http://github.com/ignertic/pybluedot",
    packages=setuptools.find_packages(),
    classifiers = ["Programming Language :: Python :: 3",
        "LICENSE :: OSI Approved :: MIT LICENSE",
        "Operating System :: OS Independent"])
