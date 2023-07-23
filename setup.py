from setuptools import setup, find_packages

setup(
    name="poetry-creator",
    version="0.1.0",
    description="The quickest way to get up and running with Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="George Pickett",
    author_email="gpickett00@gmail.com",
    url="https://github.com/grp06/poetry-creator",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
    ],
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
