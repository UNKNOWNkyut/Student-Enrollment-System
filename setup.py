from setuptools import setup, find_packages

setup(
    name='student_registration_system',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Django>=3.2',
        'djangorestframework>=3.12',
        'requests>=2.25',
    ],
)
