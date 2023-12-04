"""Setup file for Rrunning-Calculator."""
from setuptools import setup


def readme():
    """Read the README.md file."""
    with open("README.md", encoding="utf-8") as f:
        return f.read()


setup(
    name="running-calculator",
    version="1.7.0",
    description=(
        "A running distance and speed command line interface."
        " Measures in metric and imperial units,"
        " as well as marathons and half-marathons."
    ),
    long_description=readme(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    keywords="running calculator cli",
    url="https://github.com/willtheorangeguy/Running-Calculator",
    author="willtheorangeguy",
    entry_points={"console_scripts": ["running-calculator=main:main"]},
)
