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

### Run API Server

3. Activate virtual environment

    ```
    pipenv shell
    ```

3. Run API Server

    ```
    python main.py --port [PORT(default: 8000)]
    ```

### Run Tests

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

## API Docs

After run API server, navigate to the following url in your browser: http://localhost:8000/docs
