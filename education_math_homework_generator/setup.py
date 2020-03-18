#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Michael Shawn Marshall",
    author_email='physbean@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python script to generate random homework for addition and subtraction that can scale in complexity. Tools to create useful numberlines for kids to quickly practice early mathematics. ",
    entry_points={
        'console_scripts': [
            'education_math_homework_generation=education_math_homework_generation.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='education_math_homework_generation',
    name='education_math_homework_generation',
    packages=find_packages(include=['education_math_homework_generation', 'education_math_homework_generation.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/physbean/education_math_homework_generation',
    version='0.1.0',
    zip_safe=False,
)
