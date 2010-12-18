# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='acentoweb.updown',
      version=version,
      description="Rating category for voting up or down.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Israel Saeta Pérez',
      author_email='israel@acentoweb.com',
      url='http://acentoweb.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['acentoweb'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plone.contentratings',
      ],
      extras_require={
          'test': [
              'plone.app.testing',
              ]
          },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
