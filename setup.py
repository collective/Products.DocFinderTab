from setuptools import setup, find_packages
import os

version = open(os.path.join("Products", "DocFinderTab", "version.txt")).read().strip()

setup(name='Products.DocFinderTab',
      version=version,
      description="This product makes Dieter Maurer's DocFinder available from a ZMI management tab.",
      long_description=open(os.path.join("Products", "DocFinderTab", "README.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Zope2"
        ],
      keywords='Zope2 DocFinder DocFinderTab',
      author='Stefan H. Holek',
      author_email='stefan@epy.co.at',
      url='http://plone.org/products/docfindertab',
      license='ZPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
