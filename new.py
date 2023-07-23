import os
import subprocess

def create_project():
    # Get the project name from the user
    project_name = input("Enter the project name: ")

    # Create a new directory with the provided project name
    os.mkdir(project_name)

    # Navigate into the project directory
    os.chdir(project_name)

    # Initialize a new Poetry project in the directory
    subprocess.run(["poetry", "init", "--no-interaction"], check=True)

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

def install_dependencies():
    subprocess.run(["poetry", "install"], check=True)


def run_uvicorn():
    # Run the FastAPI project with uvicorn with reloading
    # Here we use `os.system` to keep the process in the foreground
    os.system(f"poetry run uvicorn main:app --reload")


if __name__ == "__main__":
    project_name = create_project()
    install_dependencies()
    run_uvicorn()