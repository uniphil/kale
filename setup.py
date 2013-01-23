try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

setup(
    name='kale',
    description='store things',
    version='0.0.1c',
    author='Philip Schleihauf',
    author_email='uniphil@gmail.com',
    packages=['kale'],
    install_requires=['minimongo'],
    license='GNU Public License v3',
    long_description=open('README.md').read(),
    url='https://github.com/uniphil/kale',
)
