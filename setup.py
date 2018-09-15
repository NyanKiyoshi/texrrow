#!/usr/bin/env python
from os.path import isfile

from setuptools import find_packages, setup

if isfile('README.md'):
    with open('README.md') as fp:
        long_description = fp.read()
else:
    long_description = ''


setup(
    name='texarrow',
    version='0.0.0',
    author='NyanKiyoshi',
    author_email='hello@vanille.bid',
    description=(
        'A simple python web-server to remotely control a LaTeX presentation '
        'from a mobile phone to give dynamic and powerful speeches.'),
    long_description=long_description,
    url='https://github.com/NyanKiyoshi/texrrow/',
    license='MIT',
    maintainer='NyanKiyoshi',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    data_files=[
        ('', ['README.md', 'LICENSE'])],
    keywords=[],
    extras_require={
        'mysql': ['flask-mysqldb']},
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux'
        'Operating System :: POSIX :: BSD',
        'Operating System :: POSIX :: BSD :: BSD/OS',
        'Operating System :: POSIX :: BSD :: FreeBSD',
        'Operating System :: POSIX :: BSD :: NetBSD',
        'Operating System :: POSIX :: BSD :: OpenBSD',
        'Operating System :: POSIX :: Other',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.5',
        'Framework :: Flask',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application'])
