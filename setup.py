from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
   name='dozenal',
   packages=['dozenal'],
   install_requires=requirements,
)
