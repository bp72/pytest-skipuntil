#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-skipuntil',
    version='0.2.0',
    author='Pavel Bityukov',
    author_email='pavleg.bityukov@gmail.com',
    maintainer='Pavel Bityukov',
    maintainer_email='pavleg.bityukov@gmail.com',
    license='MIT',
    url='https://github.com/bp72/pytest-skipuntil',
    description='A simple pytest plugin to skip flapping test with deadline',
    long_description=read('README.rst'),
    py_modules=['pytest_skipuntil'],
    python_requires='>=3.8',
    install_requires=['pytest>=3.8.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'skipuntil = pytest_skipuntil',
        ],
    },
)
