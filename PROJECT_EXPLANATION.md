# Project Explanation

This repository contains a Python practice project that demonstrates a small Flask application, Docker containerization, unit testing with `pytest`, and continuous integration with GitHub Actions.

## What is included

- `app/app.py`
  - A simple Flask web application.
  - Provides two routes:
    - `/` returns a JSON message.
    - `/health` returns a JSON status check.

- `requirements.txt`
  - Lists runtime dependencies needed to run the application.
  - Includes `Flask` and `python-dotenv`.

- `requirements-dev.txt`
  - Lists development dependencies required for testing.
  - Includes `pytest` and `pytest-flask`.

- `Dockerfile`
  - Builds a production-ready Docker image for the app.
  - Copies dependencies, installs them, and runs `app/app.py`.

- `tests/`
  - Contains automated tests for the Flask application.
  - `tests/test_app.py` verifies the app responses.
  - `tests/conftest.py` configures Pytest fixtures.

- `.github/workflows/ci.yml`
  - Defines a GitHub Actions workflow.
  - Runs on `push` and `pull_request` to the `main` branch.
  - Installs dev dependencies and executes `pytest`.

- `.gitignore`
  - Prevents local environment files and temporary Python files from being committed.

## How to use this project

### Run locally

1. Create a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
2. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Start the application:
   ```powershell
   python app/app.py
   ```
4. Open `http://127.0.0.1:5000/` in your browser.

### Build and run with Docker

1. Build the image:
   ```powershell
   docker build -t python-practice .
   ```
2. Run the container:
   ```powershell
   docker run -p 5000:5000 python-practice
   ```

### Run tests

1. Install development requirements:
   ```powershell
   pip install -r requirements-dev.txt
   ```
2. Run Pytest:
   ```powershell
   pytest
   ```

## Why this project is useful

- It shows how to structure a small Python service with a dedicated `app` folder.
- It demonstrates how to containerize a Python app using Docker.
- It provides a basic CI pipeline for automated testing on GitHub.
- It includes tests to verify that the app behaves correctly.
