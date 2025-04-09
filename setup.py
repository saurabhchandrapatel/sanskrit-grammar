from setuptools import setup, find_packages


setup(
    name='sanskrit-grammar',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[],  # list any dependencies here
    author='Saurabh Chandra Patel',
    author_email='vsaurabhaec@gmail.com',
    description='Python module provides functions to handle and manipulate various aspects of Sanskrit grammar, including word generation, prefixes etc',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/saurabhchandrapatel/sanskrit-grammar',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
