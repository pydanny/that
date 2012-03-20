README = """==============================
THAT - the Python anti-zen
==============================

Warning: This is a joke. Don't use these bits unless you want to be hated.

Documentation
==============

See http://that.rtfd.org

Installation
============

Installing from PyPI::

    pip install that

Or if you want to try and play with the awesome source code::

    git clone git@github.com:pydanny/that.git

Usage
======

From the Python shell::

    import that

Enjoy the wisdom!

Contributing
============

Clearly, the code that generates `THAT` is too straightforward. If you can make it better, then do so. Just don't do anything like add tests or document the code."""

import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'that',
    version = '1.0.7',
    description = 'The Anti-Zen of Python',
    license = 'BSD',
    long_description = README,
    url = 'https://github.com/pydanny/that',
    
    author = 'Daniel Greenfeld',
    author_email = 'pydanny@gmail.com',
    
    py_modules =  ['that'],
    
    classifiers = (
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Programming Language :: Cold Fusion',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',        
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',                                
        'Programming Language :: Python',
    ),
)
