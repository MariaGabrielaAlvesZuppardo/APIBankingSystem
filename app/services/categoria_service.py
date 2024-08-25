from typing import Dict
from app.models.transacao import Transacao
from app.schemas.categoria import ExtratoCategoriaResponse

class CategoriaService:
    def __init__(self):
        self.categorias = {"Alimentação": [], "Lazer": [], "Transporte": [], "Saúde": []}  # Exemplos de categorias

    def classificar_transacao(self, transacao: Transacao, categoria: str):
        if categoria in self.categorias:
            self.categorias[categoria].append(transacao)
        else:
            raise ValueError("Categoria inválida.")

    def relatorio_por_categoria(self) -> ExtratoCategoriaResponse:
        relatorio = {categoria: sum(transacao.valor for transacao in transacoes)
                     for categoria, transacoes in self.categorias.items()}
        return ExtratoCategoriaResponse(categorias=relatorio)
