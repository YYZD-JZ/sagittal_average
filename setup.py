#specify the package to be included manually 
#find_packages --> setup.py automatically include packages found in the source directory
from setuptools import setup, find_packages

setup(
    name = "sagittal_average",
    version="0.1.0",
    packages=find_packages(
        exclude=['*test']),
    install_requires=['numpy'],
    entry_points={
        'console_scripts': [
            'sagverage = sagittal_average.command:process'
        ]
    }
)