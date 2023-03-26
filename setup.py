# -*- coding: utf-8 -*-

from setuptools import setup,find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

with open(path.join(this_directory, 'CHANGES.md'), encoding='utf-8') as f:
    changes = f.read()

required = []

setup(
    setup_requires=['pbr'],
    pbr=True,
    packages = find_packages(),
    include_package_data=True,
    name='cors_serve',
    version='0.0.1',
    author='Loreto Parisi',
    author_email='loretoparisi@gmail.com',
    maintainer='Loreto Parisi',
    maintainer_email='loretoparisi@gmail.com',
    url="https://github.com/loretoparisi/cors_serve",
    description='CORS Serving with Python HTTP',
    long_description=readme + '\n\n' + changes,
    long_description_content_type='text/x-rst',
    license='MIT License',
    install_requires=required
)
