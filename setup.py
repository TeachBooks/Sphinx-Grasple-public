# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

VERSION = "v0.4.1"

LONG_DESCRIPTION = """
This package contains a [Sphinx](http://www.sphinx-doc.org/) extension
for inserting Grasple Exercises as an admonition.

This project is a fork of the original sphinx_exercise (v0.4.1) by
the Executable Book Project.
This fork is maintained and supported by Dani Balagué Guardia
"""

SHORT_DESCRIPTION = "A Sphinx extension for inserting Grasple exercises."

BASE_URL = "https://github.com/dbalague/sphinx-exercise"
URL = f"{BASE_URL}/archive/{VERSION}.tar.gz"

# Define all extras
extras = {
    "code_style": ["flake8<3.8.0,>=3.7.0", "black", "pre-commit"],
    "testing": [
        "coverage",
        "pytest>=3.6,<4",
        "pytest-cov",
        "pytest-regressions",
        "beautifulsoup4",
        "myst-nb~=0.17.1",
        "sphinx>=4,<6",
        "docutils>=0.15,<0.19",
        "texsoup",
        "matplotlib",
        "pyqrcode",
        "pypng"
    ],
    "rtd": [
        "sphinx>=4,<6",
        "sphinx-book-theme",
        "myst-nb~=0.17.1",
    ],
}

extras["all"] = set(ii for jj in extras.values() for ii in jj)

setup(
    name="sphinx-grasple",
    version=VERSION,
    python_requires=">=3.8",
    author="Daniel Balagué Guardia",
    author_email="d.balagueguardia@tudelft.nl",
    url=BASE_URL,
    download_url=URL,
    project_urls={
        "Source": BASE_URL,
        "Tracker": f"{BASE_URL}/issues",
    },
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="BSD",
    packages=find_packages(),
    install_requires=["sphinx>=4", "sphinx-book-theme", "pyqrcode", "pypng"],
    extras_require=extras,
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Plugins",
        "Environment :: Web Environment",
        "Framework :: Sphinx :: Extension",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python",
        "Topic :: Documentation :: Sphinx",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
        "Topic :: Text Processing",
        "Topic :: Utilities",
    ],
)
