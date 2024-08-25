# app/api/endpoints/relatorio.py
from fastapi import APIRouter, Depends
from app.services.relatorio_service import RelatorioService
from app.models.cliente import Cliente
from app.core.banco import Banco
from app.schemas.relatorio import RelatorioResponse

router = APIRouter()

def get_banco():
    return Banco()

@router.get("/relatorio-transacoes/")
def obter_relatorio_transacoes(cpf: str, inicio: str, fim: str, banco: Banco = Depends(get_banco)):
    cliente = banco.buscar_cliente_por_cpf(cpf)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    relatorio_service = RelatorioService()
    relatorio = relatorio_service.gerar_relatorio_transacoes(cliente, inicio, fim)
    return relatorio

# app/api/endpoints/categoria.py
from fastapi import APIRouter, Depends
from app.services.categoria_service import CategoriaService
from app.models.transacao import Transacao
from app.core.banco import Banco
from app.schemas.categoria import ExtratoCategoriaResponse

router = APIRouter()

def get_banco():
    return Banco()

@router.get("/extrato-categorias/")
def obter_extrato_categorias(cpf: str, banco: Banco = Depends(get_banco)):
    cliente = banco.buscar_cliente_por_cpf(cpf)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    categoria_service = CategoriaService()
    extrato = categoria_service.relatorio_por_categoria()
    return extrato
