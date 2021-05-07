# MicroChessAPI

Microchess REST api wrapping python's chess module

## Dependencies

This project uses pipenv. Note the following: [Version](Pipfile), [Modules](Pipfile.lock)

## Usage

1. Install pipenv

    ```
    pip install pipenv
    ```

2. Install all other dependencies

    ```
    pipenv install
    pipenv install -dev
    ```

3. Activate virtual environment

    ```
    pipenv shell
    ```

4. Execute API Server

    ```
    uvicorn main:app
    ```
