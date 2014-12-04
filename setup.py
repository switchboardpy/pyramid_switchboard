import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''

install_requires = [
    'pyramid>=1.2dev',
    'pyramid_mako',
    'switchboard>=1.1'
    ]

testing_extras = [
    'nose',
    'coverage',
    ]

docs_extras = [
    'Sphinx',
    ]

setup(name='pyramid_switchboard',
      version='2.2.1',
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
      extras_require = {
          'testing':testing_extras,
          'docs':docs_extras,
          },
      package_data={'pyramid_switchboard': ['static/css/*', 'static/font/*',
          'static/img/*', 'static/js/*', 'templates/*', 'panels/templates/*']
          },
      test_suite="pyramid_switchboard",
      entry_points='',
      )
