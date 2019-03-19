#!/usr/bin/env python

PROJECT = 'shinycli'

# Change docs/sphinx/conf.py too!
VERSION = '0.1'

from setuptools import setup, find_packages
from setuptools.command.install import install
import os

try:
    long_description = open('README.rst', 'rt').read()
except IOError:
    long_description = ''

class CustomInstallCommand(install):
    """Custom install setup to help run shell commands (outside shell) before installation"""
    def run(self):
        print(os.getcwd())
        os.system("sudo sh install_packages.sh lintr shiny")
        install.do_egg_install(self)


setup(
    name=PROJECT,
    version=VERSION,

    description='Shiny CLI for scaffolding a Shiny App and checking if it follows a proper structure',
    long_description=long_description,

    author='Chander Prabh Jain',
    author_email='chanderprabhjain95@gmail.com',


    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.6',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 ],

    platforms=['Any'],

    provides=[],
    cmdclass={'install': CustomInstallCommand} ,
    install_requires=['cliff', 'pathlib'],
    # scripts=['install_r_packages.sh'],
    

    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'shiny = shinycli.main:main'
        ],
        'shiny': [
            'makeshiny = shinycli.commands:Makeshiny',
            'makealgo = shinycli.commands:MakeAlgo',
            'checkapp = shinycli.commands:SanityCheck',
            'runapp = shinycli.commands:RunShiny',
        ],
    },

    zip_safe=False,
)
