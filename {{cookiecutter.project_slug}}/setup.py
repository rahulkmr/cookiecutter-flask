#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='{{cookiecutter.project_slug}}',
      version='1.0',
      packages=find_packages(),
      package_data={
          '': ['templates/**/*', 'static/**/*', 'assets/**/*']
      },
      zip_safe=False,
      )
