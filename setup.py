# setup 

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='plotly_dj',
    version='0.1.0',
    description='Plotly tools',
    packages=['plotly_dj'],
    install_requires=requirements)
