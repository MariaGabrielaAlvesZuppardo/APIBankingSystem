from fastapi import APIRouter, HTTPException, Depends
from app.services.bank_service import BankService

router = APIRouter()

def get_bank_service():
    return BankService()

@router.get("/statement/{cpf}")
def get_statement(cpf: str, bank_service: BankService = Depends(get_bank_service)):
    try:
        statement = bank_service.get_statement(cpf)
        return {"statement": statement}
    except HTTPException as e:
        raise e
