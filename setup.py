from setuptools import setup

VERSION = "0.2.1"
DESCRIPTION = "Contains classes to represent a workflow, and provide options to convert to CWL / WDL"

######## SHOULDN'T NEED EDITS BELOW THIS LINE ########

with open("./Pipeline/README.md") as readme:
    long_description = readme.read()

setup(
    name="portable-pipelines",
    version=VERSION,
    description=DESCRIPTION,
    url="https://github.com/PMCC-BioinformaticsCore/pipelines",
    author="Michael Franklin, Evan Thomas, Mohammad Bhuyan",
    author_email="michael.franklin@petermac.org",
    license="GNU",
    packages=["Pipeline"],
    zip_safe=False,
    long_description=long_description,
    long_description_content_type="text/markdown",
)