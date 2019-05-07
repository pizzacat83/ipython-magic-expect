#!/usr/bin/env python

from distutils.core import setup

setup(name='Expect',
      version='0.1.0',
      description='An IPython magic to assert the output of a cell',
      author='pizzacat83',
      author_email='pizzacat83.cpp@gmail.com',
      url='https://github.com/pizzacat83/jupyter-magic-expect',
      license='MIT',
      packages=['expectmagic'],
      install_requires=['ipython'],
      keywords=['ipython', 'assert', 'test', 'jupyter', 'notebook']
     )
