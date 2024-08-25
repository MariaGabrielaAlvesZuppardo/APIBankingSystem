from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_cliente():
    # Testa a criação de um cliente
    response = client.post("/clientes/", json={
        "name": "João Silva",
        "date_of_birth": "1990-01-01",
        "cpf": "12345678901",
        "address": "Rua A, 123 - Bairro B - Cidade C - SP"
    })
    assert response.status_code == 200
    assert "name" in response.json()
    assert response.json()["name"] == "João Silva"
    assert response.json()["date_of_birth"] == "1990-01-01"
    assert response.json()["cpf"] == "12345678901"
    assert response.json()["address"] == "Rua A, 123 - Bairro B - Cidade C - SP"
