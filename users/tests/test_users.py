import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    # Teste para criação de usuário
    response = client.post("/users", json={"id": 1, "name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}

def test_get_users():
    # Teste para listar usuários
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Verifica se a resposta é uma lista
