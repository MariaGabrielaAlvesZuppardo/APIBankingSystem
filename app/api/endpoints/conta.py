from fastapi import APIRouter, HTTPException
from app.schemas.conta import ContaCreate 
from app.services.banco_service import BancoService 

router = APIRouter()
banco_service = BancoService ()

@router.post("/")
def create_conta(conta_create: ContaCreate):
    try:
        conta = banco_service.criar_conta_corrente(conta_create.cpf, conta_create.saldo_inicial)
        return conta
    except HTTPException as e:
        raise e