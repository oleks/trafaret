from setuptools import setup, find_packages
import os
import sys


if sys.version_info < (3, 3):
    sys.exit("trafaret requires Python >= 3.3.")


def readsybling(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="trafaret",
    description="A templating engine for programming exercises",
    install_requires=[
        "click>=6.7",
        "pyyaml>=3.12"
    ],
    keywords=["trafaret", "programming", "exercises", "teaching"],
    long_description=readsybling('README.rst'),
    url="https://github.com/oleks/trafaret",
    version='version=0.0.1',
    packages=find_packages(),
    maintainer="Oleks",
    maintainer_email="oleks@oleks.info",
    license="EUPLv1.1",
    entry_points={
        'console_scripts': [
            'trafaret = trafaret.cli:main'
        ]
    },
)
