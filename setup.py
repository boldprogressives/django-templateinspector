from setuptools import setup, find_packages
import sys, os

version = '0.1'

try:
    long_description = open("README.txt").read()
except:
    long_description = ""

setup(name='django-templateinspector',
      version=version,
      description="Find out what context variables are expected by a Django Template",
      long_description=long_description,
      classifiers=[], 
      keywords='',
      author='Ethan Jucovy',
      author_email='ejucovy@gmail.com',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
