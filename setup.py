import sys
from setuptools import setup

extra = {}

if sys.version_info < (3, 3):
    sys.exit("Sorry, Python < 3.3 is not supported.")

setup(
    name='yajl',
    version='0.1',
    license='BSD',
    url='https://github.com/dgs3/yajl',
    author='Dave Sayles',
    author_email='sayles.dave@gmail.com',
    description='Module to discover and lint json files.',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=["yajl"],
    **extra
)
