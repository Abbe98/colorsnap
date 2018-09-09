from setuptools import setup, find_packages
from os import path

version = '1.1.0'
repo = 'colorsnap'

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'colorsnap',
    packages = find_packages(),
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    python_requires='>=3.6.0',
    version = version,
    description = 'Python package for snaping/rounding colors to other colors/palettes.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author = 'Albin Larsson',
    author_email = 'albin.larsson@raa.se',
    url = 'https://github.com/riksantikvareambetet/' + repo,
    download_url = 'https://github.com/riksantikvareambetet/' + repo + '/tarball/' + version,
    keywords = ['heritage', 'cultural'],
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Intended Audience :: Developers',
        'Intended Audience :: Education'
    ]
)