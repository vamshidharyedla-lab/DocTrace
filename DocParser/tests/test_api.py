from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "DocQA API"

def test_sections():
    response = client.get("/sections")
    assert response.status_code == 200

def test_search():
    response = client.get("/search?q=battery")
    assert response.status_code == 200

def test_selection():
    response = client.post("/selections", json={"name": "test", "node_ids": [1, 2]})
    assert response.status_code == 200
