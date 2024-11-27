import pytest
from fastapi.testclient import TestClient
from auth.main import app  # Corrigido: agora importa corretamente o 'app' de 'main.py' em auth/

client = TestClient(app)

def test_login_success():
    # Teste de sucesso: enviar credenciais válidas
    response = client.post("/token", json={"username": "admin", "password": "123"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_failure():
    # Teste de falha: enviar credenciais inválidas
    response = client.post("/token", json={"username": "wrong", "password": "1234"})
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid credentials"}
