
# Poetry Creator

Poetry Creator is a Python package that makes it super easy to get started with a new Poetry project. It helps you initialize a new project with a basic structure and install some common Python packages that you might need.

## Installation

To install Poetry Creator, simply run:

`pip install poetry-creator` 

## Usage

Once Poetry Creator is installed, you can use it to create a new project like this:

`poetry-creator my_project_name` 

This command will:

1.  Create a new directory called `my_project_name`.
2.  Initialize a new Poetry project in that directory.
3.  Create a `pyproject.toml` file with the required dependencies.
4.  Initialize a basic FastAPI project structure.

The `pyproject.toml` file includes dependencies for a variety of common Python packages, including:

-   FastAPI
-   Uvicorn
-   Gunicorn
-   OpenAI and OpenAI-Async
-   Redis
-   Black
-   Termcolor
-   Python-dotenv
-   Websockets
-   Aiofiles
-   Loguru
-   Webrtcvad

After creating the project, Poetry Creator will automatically install these dependencies and then run your new project using Uvicorn.

Remember to replace `"<your name here> <your email here>"` in the `pyproject.toml` file with your actual name and email.

## Errors

If there's a problem during project creation (for example, if the project directory already exists), Poetry Creator will print an error message and exit.