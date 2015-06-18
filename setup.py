import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''

install_requires = [
    'pyramid',
    'pyramid_mako',
    'switchboard>=1.3.3'
    ]

setup(name='pyramid_switchboard',
      version='0.5',
      description=('A package which wraps the switchboard feature flipper '
                   'for Pyramid application development'),
      long_description=README,
      classifiers=[
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP :: WSGI",
          "License :: OSI Approved :: Apache Software License",
      ],
      keywords='wsgi pylons pyramid featureflipper',
      author=("Kyle Adams"),
      author_email="kadams54@gmail.com",
      url="https://github.com/switchboardpy/pyramid_switchboard",
      license="Apache License",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      entry_points='',
      )
