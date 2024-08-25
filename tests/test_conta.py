from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_conta():
    response = client.post("/contas/", json={
        "cpf": "12345678901",
        "saldo_inicial": 1000.0
    })
    assert response.status_code == 200
    assert "numero" in response.json()
