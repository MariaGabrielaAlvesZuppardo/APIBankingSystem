from fastapi import APIRouter, HTTPException, Depends
from app.schemas.transaction import TransactionCreate
from app.services.bank_service import BankService

router = APIRouter()

def get_bank_service():
    return BankService()

@router.post("/transactions/")
def create_transaction(transaction_create: TransactionCreate, bank_service: BankService = Depends(get_bank_service)):
    try:
        message = bank_service.perform_transaction(
            transaction_create.cpf,
            transaction_create.type,
            transaction_create.value
        )
        return {"message": message}
    except HTTPException as e:
        raise e
