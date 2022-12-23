# file: setup.py
from distutils.core import setup

# from setuptools import setup
# from setuptools.extension import Extension
from Cython.Build import cythonize

setup(name='Hello world app',
      ext_modules=cythonize("hello.pyx"))
