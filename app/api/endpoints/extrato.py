from fastapi import APIRouter, HTTPException
from app.services.banco_service import BancoService

router = APIRouter()
banco_service = BancoService()

@router.get("/{cpf}")
def get_extrato(cpf: str):
    try:
        extrato = banco_service.exibir_extrato(cpf)
        return {"extrato": extrato}
    except HTTPException as e:
        raise e
