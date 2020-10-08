from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

classifiers = [
    'Intended Audience :: Education',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='googlesheets_to_scatterplot',
    version='0.0.1',
    description='We can create plots directly from Google Sheets',
    long_description= long_description + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://github.com/vatanpatel/googlesheets_to_scatterplot',
    author='Vatan Patel',
    author_email='i12vatanp@iimidr.ac.in',
    license='MIT',
    classifiers=classifiers,
    keywords='googlesheets',
    packages=find_packages(),
    install_requires=['pandas', 'matplotlib', 'seaborn', 'gspread', 'oauth2client']
)