from setuptools import setup
import py2exe

with open("README.markdown", "r") as fh:
    long_description = fh.read()

setup(
    name='pokemon-tv',
    version='0.0.2',
    packages=['pokemon-tv', 'pokemon-tv.ytdl', 'pokemon-tv.ytdl.extractor', 'pokemon-tv.ytdl.downloader', 'pokemon-tv.ytdl.extractortest',
              'pokemon-tv.ytdl.postprocessor'],
    url='https://github.com/davFaithid/pokemon-tv',
    license='',
    author='davFaithid',
    author_email='',
    description='Watch (currently only the first season) of Pokemon in python3.',
    console=['pokemon-tv/__init__.py'],
    options={
            "py2exe":{
                    "unbuffered": True,
                    "optimize": 2,
                    "excludes": ["email"]
                }
        }
)
