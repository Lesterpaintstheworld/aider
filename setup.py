from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    package_data={"aider": ["queries/*.scm"]},
    include_package_data=True,
)
