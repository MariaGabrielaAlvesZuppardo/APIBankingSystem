from fastapi import APIRouter, HTTPException
from app.schemas.transacao import TransacaoCreate 
from app.services.banco_service import BancoService 

router = APIRouter()
banco_service = BancoService()

@router.post("/")
def create_transacao(transacao_create: TransacaoCreate):
    try:
        mensagem = banco_service.realizar_transacao(transacao_create.cpf, transacao_create.tipo, transacao_create.valor)
        return {"mensagem": mensagem}
    except HTTPException as e:
        raise e