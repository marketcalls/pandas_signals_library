
from setuptools import setup, find_packages

setup(
    name='pandas-signals',
    version='1.0.5',
    description='Signal processing utilities for Pandas',
    author='Rajandran R',
    author_email='rajandran@marketcalls.in',
    url='https://github.com/marketcalls/pandas-signals',
    packages=find_packages(),
    install_requires=['pandas'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
