from setuptools import setup, find_packages

setup(
    name="aider_nova",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Ajoutez ici les dépendances nécessaires
    ],
    entry_points={
        'console_scripts': [
            'aider_nova=aider_nova.main:main',
        ],
    },
)
