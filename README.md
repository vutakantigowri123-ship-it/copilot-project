# Python Practice Project

A simple Python practice project with Docker and GitHub Actions.

## Features

- Flask web app
- Docker containerization
- GitHub Actions CI for tests
- Unit tests with pytest

## Getting Started

### Build locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app/app.py
```

### Build with Docker

```powershell
docker build -t python-practice .
docker run -p 5000:5000 python-practice
```

### Run tests

```powershell
pip install -r requirements-dev.txt
pytest
```
