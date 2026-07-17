# DocQA System

AI-powered document QA system for medical device manuals.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
export GEMINI_API_KEY=your_key
uvicorn app.main:app --reload
```

## Test

```bash
pytest
```

## API Endpoints

- GET /sections - list top-level sections
- GET /node/{id} - get node details
- GET /search?q=term - search nodes
- GET /diff/node/{id}?from=1&to=2 - compare versions
- POST /selections - save node selection
- GET /selections/{id} - get selection
- POST /generate-tests - generate QA tests
- GET /tests/{id} - get tests with stale flag
- GET /retrieve-tests - retrieve all tests
