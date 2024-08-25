from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_transacao():
    response = client.post("/transacoes/", json={
        "cpf": "12345678901",
        "tipo": "depósito",
        "valor": 500.0
    })
    assert response.status_code == 200
    assert "mensagem" in response.json()
