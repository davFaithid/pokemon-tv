from setuptools import setup

setup(
    name='pokemon-tv',
    version='0.0.1',
    packages=['src', 'src.ytdl', 'src.ytdl.extractor', 'src.ytdl.downloader', 'src.ytdl.extractortest',
              'src.ytdl.postprocessor'],
    url='https://github.com/davFaithid/pokemon-tv',
    license='',
    author='davFaithid',
    author_email='',
    description='Watch (currently only the first season) of Pokemon in python3.'
)
