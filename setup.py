# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
long_description = "Python RFC 4648 base32hex implementation"

setup(
    name='base32hex',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.2',

    description='RFC 4648 Extended Hex Alphabet',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/graham/base32hex',

    # Author details
    author='Graham Abbott',
    author_email='graham.abbott@gmail.com',

    # Choose your license
    license='MIT',

    py_modules=['base32hex'],
    download_url="https://github.com/graham/base32hex/tarball/0.3",
)
