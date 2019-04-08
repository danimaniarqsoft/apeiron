from setuptools import setup, find_packages
from apeiron.reader import add

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(name='apeiron',
      version='0.0.1',
      description='The apeiron cli',
      long_description=readme,
      url='https://github.com/danimaniarqsoft/apeiron-cli',
      author='Daniel Cortes Pichardo',
      license=license,
      packages=find_packages(exclude=('tests', 'docs')),
      zip_safe=False)
