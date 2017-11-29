#!/usr/bin/env python

# -*- coding: utf-8 -*-

import os.path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


exec(open('dacase/version.py').read())

classifiers = """
'Development Status :: 2 - Alpha',
'Intended Audience :: Developers',
'Natural Language :: English',
'Programming Language :: Python :: 2',
'Programming Language :: Python :: 2.7',
'Programming Language :: Python :: 3',
'Programming Language :: Python :: 3.2',
'Programming Language :: Python :: 3.3',
'Programming Language :: Python :: 3.4',
'Programming Language :: Python :: 3.5',
"""


tests_require = [
    'coverage',
    'flake8',
    'pydocstyle',
    'pylint',
    'pytest-pep8',
    'pytest-cov',
    # for pytest-runner to work, it is important that pytest comes last in
    # this list: https://github.com/pytest-dev/pytest-runner/issues/11
    'pytest'
]

version = '0.1.0'

setup(name='dacase',
      version=__version__,
      description='serves purposes',
      long_description=read('README.rst'),
      author='dbl0null',
      author_email='dbl0null@gmail.com',
      url='https://github.com/dbl0null/dacase',
      classifiers=[c.strip() for c in classifiers.splitlines()
                   if c.strip() and not c.startswith('#')],
      include_package_data=True,
      packages=[
          'dacase',
          ],
      test_suite='tests',
      setup_requires=['pytest-runner'],
      tests_require=tests_require)
