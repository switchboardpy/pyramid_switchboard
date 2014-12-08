import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''

install_requires = [
    'pyramid',
    'pyramid_switchboard',
    'switchboard',
    'pymongo',
]

setup(
    name='switchboard_demo',
    version='0.1',
    description='A demo application for Switchboard',
    long_description=README,
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "License :: OSI Approved :: Apache Public License",
    ],
    keywords='web wsgi pylons pyramid',
    author="Kyle Adams",
    author_email="kadams54@gmail.com",
    url="https://github.com/switchboardpy/switchboard_pyramid",
    license="Apache license",
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
)
