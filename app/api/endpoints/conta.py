from fastapi import APIRouter, HTTPException, Depends
from app.schemas.account import AccountCreate
from app.services.bank_service import BankService

router = APIRouter()

def get_bank_service():
    return BankService()

@router.post("/accounts/")
def create_account(account_create: AccountCreate, bank_service: BankService = Depends(get_bank_service)):
    try:
        account = bank_service.create_current_account(
            account_create.cpf,
            account_create.initial_balance
        )
        if not account:
            raise HTTPException(status_code=400, detail="Client not found.")
        return account
    except HTTPException as e:
        raise e
