# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), encoding='utf-8') as f:
    readme = f.read()

with open(path.join(this_directory, 'CHANGES.rst'), encoding='utf-8') as f:
    changes = f.read()

required = ['future', 'six', 'numpy', 'bitarray']

setup(
    name='cors_serve',
    version='0.0.1',
    packages=['cors_serve'],
    author='Loreto Parisi',
    author_email='loretoparisi@gmail.com',
    maintainer='Loreto Parisi',
    maintainer_email='loretoparisi@gmail.com',
    url="https://github.com/loretoparisi/cors_serve",
    description='CORS Serving with Python',
    long_description=readme + '\n\n' + changes,
    long_description_content_type='text/x-rst',
    license='MIT License',
    install_requires=required
