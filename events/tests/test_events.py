import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_event():
    # Teste para criar evento
    response = client.post("/events", json={"title": "Meeting"})
    assert response.status_code == 200
    assert response.json()["title"] == "Meeting"

def test_get_events():
    # Teste para listar eventos
    response = client.get("/events")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Verifica se a resposta é uma lista
