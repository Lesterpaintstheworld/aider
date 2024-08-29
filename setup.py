from setuptools import setup, find_packages

setup(
    name="aider",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Ajoutez ici les dépendances nécessaires
        "streamlit",
        "typer",
    ],
    entry_points={
        'console_scripts': [
            'aider=aider.main:main',
        ],
    },
)
