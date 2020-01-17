from setuptools import setup
import py2exe

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pokemon-tv',
    version='0.2',
    packages=['pokemon-tv'],
    data_files=[('icon', ['pokemon-tv/icon.png'])]
    url='https://github.com/davFaithid/pokemon-tv',
    license='GPL-3.0',
    author='davFaithid',
    author_email='',
    description='Watch Pokemon in python3.',
    console=['pokemon-tv/__init__.py'],
    options={
            "py2exe":{
                    "unbuffered": True,
                    "optimize": 2,
                    "excludes": ["email"]
                }
        }
)
