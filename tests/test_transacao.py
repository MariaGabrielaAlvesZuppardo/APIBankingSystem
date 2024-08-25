from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_transacao():
    # Testa a criação de uma transação
    response = client.post("/transacoes/", json={
        "cpf": "12345678901",
        "tipo": "depósito",
        "valor": 500.0
    })
    assert response.status_code == 200
    data = response.json()
    assert "mensagem" in data
    assert data["mensagem"] == "Transação realizada com sucesso."
