from setuptools import setup, find_packages

setup(
    name='skbu-2nd-sem',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pytest==6.2.4',
        'pytest-cov==2.12.1',
    ],
    author='Pabitra Banerjee',
    author_email='pabitra.banerjee@explorecode.live',
    description='A Python package for implementing data structures and algorithms for SKBU 2nd semester syllabus.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/PB2204/SKBU-2nd-Sem',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)