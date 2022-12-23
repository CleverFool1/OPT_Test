# file: setup.py
from distutils.core import setup

# from setuptools import setup
# from setuptools.extension import Extension
from Cython.Build import cythonize

setup(name='cy_utils app',
      ext_modules=cythonize("cy_utils.pyx") )