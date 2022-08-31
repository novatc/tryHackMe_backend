"""
Setup file for building binaries
"""
from setuptools import setup, find_packages

setup(name='try_hack_me',
    version='1.0',
    packages=find_packages(include=['modules', 'modules.*', 'Ashok', 'Ashok.*', 'wafw00f', 'wafw00f.*']),
    classifiers=[
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    ]
)
