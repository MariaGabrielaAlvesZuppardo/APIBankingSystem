from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_conta():
    # Testa a criação de uma conta
    response = client.post("/contas/", json={
        "cpf": "12345678901",
        "saldo_inicial": 1000.0
    })
    assert response.status_code == 200
    data = response.json()
    assert "numero" in data
    assert "agencia" in data
    assert data["saldo"] == 1000.0
