from setuptools import setup, find_packages

# We read the contents of our README file
with open("README.md") as fh:
    long_description = fh.read()              # We read the contents of our README file into long_discription

# We define the classifiers
classifiers = [
    'Intended Audience :: Education',          # We created this module to serve educational purpose
    'Operating System :: OS Independent',      # We can use this module on any OS
    'License :: OSI Approved :: MIT License',  # The most widely used open source licence
    'Programming Language :: Python :: 3'      # The programming language for the module is Python
]

# Now we are good to setup our module
setup(
    name='googlesheets_to_scatterplot',                                                         # We define the name of our module
    version='0.0.12',                                                                           # We define the version. We update this everytime we make a change
    description='We can create plots directly from Google Sheets',                              # We define the short discription
    long_description= long_description,                                                         # We define the long distribution by adding long_discription variable
    long_description_content_type="text/markdown",                                              # We set the content type of our README file
    url='https://github.com/vatanpatel/googlesheets_to_scatterplot',                            # We add the git url for reference
    author='Vatan Patel',                                                                       # We add the author name
    author_email='i12vatanp@iimidr.ac.in',                                                      # We add the author email for people to get in touch
    license='MIT',                                                                              # We define the type od licence we have added
    classifiers=classifiers,                                                                    # We add our defined classifiers here
    keywords='googlesheets',                                                                    # We add keywords people can use to search this module
    packages=find_packages(),                                                                   # We want our module to find the packages required to run
    install_requires=['markdown', 'pandas', 'matplotlib', 'seaborn', 'gspread', 'oauth2client']  # We define the modules required to run our module
)