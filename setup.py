import os
import re
import logging
import setuptools


def read(file):
    return open(file, "r", encoding="utf-8").read()


def get_meta_attr(attr: str) -> str:
    """
    Return package meta attribute listed into {package_dir}/__init__.py.
    """
    init_py = read(os.path.join("processpool", "__init__.py"))
    pattern = f"{attr} = ['\"]([^'\"]+)['\"]"
    try:
        return re.search(pattern, init_py).group(1)
    except AttributeError as err:
        logging.error(err)


title = get_meta_attr("__title__")
version = get_meta_attr("__version__")
url = get_meta_attr("__url__")
author = get_meta_attr("__author__")
author_email = get_meta_attr("__author_email__")


setuptools.setup(
    name=title,
    version=version,
    url=url,
    description="A very cool process manager.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author=author,
    author_email=author_email,
    packages=setuptools.find_packages(
        ".",
        exclude=("tests",),
    ),
    python_requires=">=3.8.0",
    install_requires=[
        "click==8.0.1",
    ],
)
