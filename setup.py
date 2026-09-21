from setuptools import find_packages,setup
from typing import List

def get_requirement()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []

    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()

            for line in lines:
                requirement=line.strip()
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("file not found")

        return requirement_list
print(get_requirement())
setup(
    name="AI-TRAVEL-PLANNER",
    version="0.1.0",
    author="akash",
    author_email="akash.karma24@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement()

)
        