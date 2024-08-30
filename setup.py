from setuptools import setup, find_packages

setup(
    name="aider-chat",
    packages=find_packages(where="."),
    package_dir={"": "."},
    package_data={"aider": ["queries/*.scm"]},
    include_package_data=True,
)
