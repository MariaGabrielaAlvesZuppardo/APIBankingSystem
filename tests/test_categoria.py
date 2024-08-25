from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_obter_extrato_categorias():
    response = client.get("/categorias/extrato-categorias/", params={
        "cpf": "12345678901"
    })
    assert response.status_code == 200
    assert "categorias" in response.json()
