#!/usr/bin/env python

"""The setup script."""

from os import path
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

here = path.abspath(path.dirname(__file__))

# get the dependencies and installs

with open(
    path.join(here, "requirements.txt"), encoding="utf-8"
) as f:
    all_reqs = f.read().split("\n")

install_requires = [
    x.strip() for x in all_reqs if "git+" not in x
]
dependency_links = [
    x.strip().replace("git+", "")
    for x in all_reqs
    if x.startswith("git+")
]

test_requirements = [ ]

setup(
    author="T. Moudiki",
    author_email='thierry.moudiki@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Boosted Configuration Networks",
    install_requires=install_requires,
    dependency_links=dependency_links, 
    license="BSD license",
    long_description="Boosted Configuration (neural) Networks for supervised learning", #readme + '\n\n' + history,
    include_package_data=True,
    keywords=['BCN', 'Machine Learning', 'Statistical Learning'],
    name='BCN',
    packages=find_packages(include=['BCN', 'BCN.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Techtonique/bcn_python',
    version='0.5.0',
    zip_safe=False,
)
