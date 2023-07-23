from setuptools import setup, find_packages

setup(
    name="poetry creator",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'create-poetry = poetry_creator.create_poetry:main',
        ],
    },
    install_requires=[
        'poetry',
    ],
)
