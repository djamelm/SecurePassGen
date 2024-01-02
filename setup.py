from setuptools import setup, find_packages

setup(
    name='generateur_mot_de_passe',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyperclip==1.8.2',
    ],
)
