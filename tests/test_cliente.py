from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_cliente():
    response = client.post("/clientes/", json={
        "nome": "João Silva",
        "data_nascimento": "1990-01-01",
        "cpf": "12345678901",
        "endereco": "Rua A, 123 - Bairro B - Cidade C - SP"
    })
    assert response.status_code == 200
    assert "nome" in response.json()
