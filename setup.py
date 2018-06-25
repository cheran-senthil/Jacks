from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='Jacks',
      version='0.1.0',
      description='Basic Commands for Poker',
      long_description=readme(),
      url='https://github.com/Cheran-Senthil/Jacks',
      author='Cheran and Mukundan',
      license='Apache License 2.0',
      packages=['jacks'],
      install_requires=[
          'six',
          'termcolor',
      ])
