# Project Overview

This project is a web application that allows users to manage their tasks and to-do lists. It is built using React and Node.js, and uses MongoDB for data storage.

## Folder Structure

- `.pre-commit-config.yaml`: Configuration file for pre-commit hooks.
- `.github/`: Contains GitHub-related files, including issue templates and workflows.
- `.gitignore`: Specifies files and directories that should be ignored by Git.
- `README.md`: This file, which provides an overview of the project.
- `docker-compose.yml`: Docker Compose file for setting up the application environment.
- `music_teams_src/`: Contains outdated source code for the app development with Flutter.
- `backend/`: Contains the environment, requirements files for the backend and source code folders.
- `backend/env_template`: Template for environment variables used in the backend.
- `backend/requirements.txt`: Contains the Python dependencies for the backend.
- `backend/Dockerfile`: Dockerfile for building the backend image.
- `backend/tests/`: Contains test files for the backend.
- `backend/monolith`: Contains the monolithic backend source code.
- `backend/monolith/database`: Contains database connection functions.
- `backend/monolith/models`: Contains data models for the backend.
- `backend/monolith/routes`: Contains the API routes for the backend.
- `backend/monolith/utils`: Contains utility functions for the backend.

## Libraries and Frameworks

- Flutter for the frontend / app development.
- Python FastAPI for the backend.
- MySQL for data storage.

## Coding Standards

- Use try except blocks for error handling inside functions.
- Try to pass the pre-commit checks before pushing code.
- Every PR made should be done from a new branch that is based on `nikos-dev` branch 
and will be merged into `nikos-dev` branch.

## UI guidelines

- A toggle is provided to switch between light and dark mode.
- Application should have a modern and clean design.

## guidelines
- `/backend/monolith/routes`: Here are the API routes for the backend. 
Be sure that for each route, the function is defined and the necessary imports are made.
Also, ensure that the routes are properly registered in the FastAPI application in `/backend`.
Do not make db queries directly in the routes; instead, use the functions defined in `/backend/monolith/utils`.
Also import only the necessary models from `/backend/monolith/models` 
(do not import models that inherit from Base class -
instead import models that inherit BaseModel class).
- `/backend/monolith/utils`: Contains utility functions for the backend.
Here you can define functions that interact with the database (queries, CRUD operations).
Return something like Tuple[bool, str] for success or failure,
or Tuple[bool, str, Any] if you want to return some data,
or Tuple[Optional[DefinedModel], str] if you want to return a model instance
(where DefinedModel is a class derived from BaseModel).
- `backend/tests/`: Contains test files for the backend.
Make sure to write tests that leave the database in the same state as before the test.
For example, if you login in the test, make sure to logout after the test.
You can use the setUp and tearDown methods in the test classes to prepare the database before each test and clean it up after each test.
Direct database queries are not allowed in the tests. 
Everything should be done through requests to the API routes defined in `/backend/monolith/routes`,
assuming the app is up and running.
- You are free to add new files with code in the `backend/monolith/routes` and `backend/monolith/utils` and `backend/tests` folders,
but if you want to change anything in `backend/monolith/database` or `backend/monolith/models`, please discuss it first (mention me in the github PR / Issue).
- Run the workflows on the branch you are working on.