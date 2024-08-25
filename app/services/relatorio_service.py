# app/services/relatorio_service.py
from typing import List
from app.models.cliente import Cliente
from app.models.transacao import Transacao
from app.schemas.relatorio import RelatorioResponse

class RelatorioService:
    def gerar_relatorio_transacoes(self, cliente: Cliente, inicio: str, fim: str) -> RelatorioResponse:
        transacoes = [transacao for conta in cliente.contas for transacao in conta.historico 
                      if inicio <= transacao.data_hora.strftime("%Y-%m-%d") <= fim]
        total = sum(transacao.valor for transacao in transacoes)
        return RelatorioResponse(transacoes=[{
            "data": transacao.data_hora.strftime("%Y-%m-%d"),
            "tipo": transacao.tipo,
            "valor": transacao.valor
        } for transacao in transacoes], total=total)

# app/services/categoria_service.py
from typing import Dict
from app.models.transacao import Transacao
from app.schemas.categoria import ExtratoCategoriaResponse

class CategoriaService:
    def __init__(self):
        self.categorias = {"Alimentação": [], "Lazer": [], "Transporte": []}

    def classificar_transacao(self, transacao: Transacao, categoria: str):
        if categoria in self.categorias:
            self.categorias[categoria].append(transacao)
        else:
            raise ValueError("Categoria inválida.")

    def relatorio_por_categoria(self) -> ExtratoCategoriaResponse:
        relatorio = {categoria: sum(transacao.valor for transacao in transacoes)
                     for categoria, transacoes in self.categorias.items()}
        return ExtratoCategoriaResponse(categorias=relatorio)
