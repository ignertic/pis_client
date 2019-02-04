import setuptools

with open("README.md", 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="pybluedot",
    author="Gishobert Gwenzi",
    author_email="ilovebugsincode",
    version="0.1.0",
    description="BluedotSMS python wrapper",
    long_description=long_description,
    url="http://github.com/ignertic/pybluedot",
    packages=setuptools.find_packages(),
    install_requires=['loguru', 'requests'],
    entry_points={"console_scripts" : ["sms=pybluedot.__main__:main" ]},
    classifiers = ["Programming Language :: Python :: 3",
        "LICENSE :: OSI Approved :: MIT LICENSE",
        "Operating System :: OS Independent"])
