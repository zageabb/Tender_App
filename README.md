# Reflex Tendering Assistant App

This project contains a FastAPI backend and a minimal Reflex frontend. The backend provides authentication and tender management APIs while the Reflex frontend demonstrates how to build the UI using pure Python.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

## Backend

Run the API with:

```bash
uvicorn app.main:app --reload
```

## Frontend

To start the Reflex development server:

```bash
reflex run
```

The frontend code lives in `tender_frontend/` with the configuration in `rxconfig.py`.

## Tests

Run tests with:

```bash
pytest
```
