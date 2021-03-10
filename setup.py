#!/usr/bin/env python

from setuptools import setup

setup(
    name='python-nginx-fm',
    version='1.5.4',
    description='Create and modify nginx serverblock configs in Python',
    author='Jacob Cook',
    author_email='jacob@peakwinter.net',
    url='https://github.com/quanghuy1288/python-nginx',
    py_modules=['nginx'],
    keywords=['nginx', 'web servers', 'serverblock', 'server block'],
    download_url='https://github.com/quanghuy1288/python-nginx/archive/1.5.4.zip',
    license='GPLv3',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: Unix",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
    ]
)
