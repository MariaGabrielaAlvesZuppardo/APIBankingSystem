from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_obter_relatorio_transacoes():
    response = client.get("/relatorios/relatorio-transacoes/", params={
        "cpf": "12345678901",
        "inicio": "2024-01-01",
        "fim": "2024-01-31"
    })
    assert response.status_code == 200
    assert "transacoes" in response.json()

# tests/test_categoria.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_obter_extrato_categorias():
    response = client.get("/categorias/extrato-categorias/", params={
        "cpf": "12345678901"
    })
    assert response.status_code == 200
    assert "categorias" in response.json()
