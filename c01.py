# setup.py
from distutils.core import setup, Extension

module = Extension('c01', sources=['c01.c'])

setup(name='PackageName',
      version='1.0',
      description='This is a package for c01',
      ext_modules=[module])
