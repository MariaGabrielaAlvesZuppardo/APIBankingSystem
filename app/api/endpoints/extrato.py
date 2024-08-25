from fastapi import APIRouter, HTTPException, Depends
from app.services.banco_service import BancoService

router = APIRouter()

def get_banco_service():
    return BancoService()

@router.get("/extrato/{cpf}")
def get_extrato(cpf: str, banco_service: BancoService = Depends(get_banco_service)):
    try:
        extrato = banco_service.exibir_extrato(cpf)
        return {"extrato": extrato}
    except HTTPException as e:
        raise e
