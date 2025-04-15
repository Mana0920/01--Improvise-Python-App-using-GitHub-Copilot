from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_generate_checksum():
    response = client.post("/generate-checksum", json={"text": "hello world"})
    assert response.status_code == 200
    assert "checksum" in response.json()

def test_welcome():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]
