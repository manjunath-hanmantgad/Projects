from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e.'
# the below function takes input for path where requirements.txt is located
def get_requirements(file_path:str)->List[str]:
    """this function returns list of all packages kept inside requirements.txt file"""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        #[r.replace("\n","")for r in requirements.txt]
        [r.replace("\n","")for r in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements
        
    
# metadata information about project
setup(
    name='end2endproject',
    version='0.1',
    author='Manjunath',
    packages=find_packages(),
    install_requirements = get_requirements('requirements.txt')
)
