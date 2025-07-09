## Contribution Guidelines

When adding a new endpoint:
1. Create the endpoint in the `routes` directory.
2. Add the endpoint router to the `app.py` file.
3. Define inputs and outputs of the endpoint, use the Pydantic models defined in the `models` directory, and only if needed, make a new model derived from `BaseModel` class.
4. Any database access should be done in functions through the `utils` directory, using the SQLAlchemy ORM. 

Ensure that you:
- add tests for the new endpoint in the `tests` directory.
- document the endpoint in the `README.md` file.
- follow the coding style and conventions used in the existing codebase (pass the pre-commit).
