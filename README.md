# MicroChessAPI

Microchess REST api wrapping python's chess module

## Dependencies

This project uses pipenv. Note the following: [Version](Pipfile), [Modules](Pipfile.lock)

## Usage

1. Install pipenv

    ```
    pip install pipenv
    ```

1. Install all other dependencies

    ```
    pipenv install
    ```

### Run api server

3. Activate virtual environment

    ```
    pipenv shell
    ```

3. Run API Server

    ```
    python main.py --port [PORT(default: 8000)]
    ```

### Run tests

3. Install dependencies for dev mode

    ```
    pipenv install -dev
    ```

3. Activate virtual environment

    ```
    pipenv shell
    ```

3. Run tests

    ```
    pytest test
    ```
