from setuptools import find_packages,setup
from typing import List

def get_requirements()->list[str]:
    requirements_list=list[str]=[]
    return requirements_list

setup(
    
    name='sensor',
    version="0.0.1",
    author="Bodhi",
    author_email="2004290@kiit.ac.in",
    packages=find_packages(),
    install_requires=get_requirements(),
)