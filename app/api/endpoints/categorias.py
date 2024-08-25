from fastapi import APIRouter, Depends, HTTPException
from app.services.categoria_service import CategoriaService
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
    
    # Classificar todas as transações do cliente em categorias
    for conta in cliente.contas:
        for transacao in conta.historico:
            # Aqui você pode definir a lógica para classificar transações em categorias específicas
            categoria = "Alimentação"  # Exemplo: você pode decidir a categoria com base na transação
            categoria_service.classificar_transacao(transacao, categoria)
    
    extrato = categoria_service.relatorio_por_categoria()
    return extrato
