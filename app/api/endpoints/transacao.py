from fastapi import APIRouter, HTTPException, Depends
from app.schemas.transacao import TransacaoCreate
from app.services.banco_service import BancoService

router = APIRouter()

def get_banco_service():
    return BancoService()

@router.post("/transacoes/")
def create_transacao(transacao_create: TransacaoCreate, banco_service: BancoService = Depends(get_banco_service)):
    try:
        mensagem = banco_service.realizar_transacao(
            transacao_create.cpf,
            transacao_create.tipo,
            transacao_create.valor
        )
        return {"mensagem": mensagem}
    except HTTPException as e:
        raise e
