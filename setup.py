from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

classifiers = [
    'Intended Audience :: Education',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='vatanbasiccalculator',
    version='0.0.1',
    description='A very basic calculator',
    long_description=long_description + open('CHANGELOG.txt').read(),
    url='',
    author='Vatan Patel',
    author_email='i12vatanp@iimidr.ac.in',
    license='MIT',
    classifiers=classifiers,
    keywords='gsheets',
    packages=find_packages(),
    install_requires=['pandas', 'matplotlib.pyplot', 'seaborn', 'gspread', 'oauth2client']
)