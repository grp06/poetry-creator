import os
import argparse
from pathlib import Path
import subprocess

def create_project(project_name):
    # Create a new directory with the provided project name
    project_dir = Path(project_name)
    if project_dir.exists():
        raise FileExistsError(f"Directory '{project_name}' already exists.")

    # Create project directory
    project_dir.mkdir(parents=True)

    # Initialize a new Poetry project in the directory
    subprocess.run(["poetry", "init", "--no-interaction"], check=True, cwd=project_dir)


    # Create a `pyproject.toml` file with the required dependencies
    pyproject_content = """
[tool.poetry]
name = "{0}"
version = "0.1.0"
description = ""
authors = ["<your name here> <your email here>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.11.4"
fastapi = "*"
uvicorn = "*"
gunicorn = "*"
openai = "*"
openai-async = "*"
redis = "*"
black = "*"
termcolor = "*"
python-dotenv = "*"
websockets = "*"
aiofiles = "*"
loguru = "*"
webrtcvad = "*"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
""".format(project_name)

    with open("pyproject.toml", "w") as f:
        f.write(pyproject_content)

    # Initialize a FastAPI project structure
    main_content = """
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
"""
    with open("main.py", "w") as f:
        f.write(main_content)

    return project_name  # return the project name for running uvicorn

def install_dependencies(project_name):
    project_dir = Path(project_name)
    subprocess.run(["poetry", "install"], check=True, cwd=project_dir)

def run_uvicorn(project_name):
    project_dir = Path(project_name)
    os.system(f"cd {project_dir} && poetry run uvicorn main:app --reload")

def check_poetry_installed():
    try:
        subprocess.run(["poetry", "--version"], check=True)
    except subprocess.CalledProcessError:
        print("Poetry is not installed, installing it now...")
        subprocess.run(["pip", "install", "poetry"], check=True)

def main():
    parser = argparse.ArgumentParser(description='Create a new Python project with Poetry.')
    parser.add_argument('project_name', type=str, help='The name of the project.')

    args = parser.parse_args()

    try:
        check_poetry_installed()
        create_project(args.project_name)
        install_dependencies(args.project_name)
        run_uvicorn(args.project_name)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()