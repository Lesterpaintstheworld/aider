from setuptools import setup, find_packages

setup(
    name="aider",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Ajoutez ici les dépendances de votre projet
    ],
    entry_points={
        'console_scripts': [
            'aider=aider.main:main',
        ],
    },
)
