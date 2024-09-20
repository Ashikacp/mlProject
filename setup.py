from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .' #line in requirements.txt that specifies editable installation (-e .).

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) # -e . is used for local development and should not be included in the list of requirements to be processed by setup.py
    
    return requirements    
    

setup(
    name='mlproject',
    version='0.0.1',
    author='Ashika',
    author_email='ashikacp2012@gmail.com',
    packages=find_packages(),  #function automatically discovers all packages and subpackages. It looks for __init__.py files to identify them.
    install_requires=get_requirements('requirements.txt')
)