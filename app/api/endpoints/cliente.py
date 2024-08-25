from fastapi import APIRouter, HTTPException, Depends
from app.schemas.client import ClientCreate
from app.services.bank_service import BankService

router = APIRouter()

def get_bank_service():
    return BankService()

@router.post("/clients/")
def create_client(client_create: ClientCreate, bank_service: BankService = Depends(get_bank_service)):
    try:
        client = bank_service.register_client(
            client_create.name,
            client_create.birth_date,
            client_create.cpf,
            client_create.address
        )
        if not client:
            raise HTTPException(status_code=400, detail="Client already registered.")
        return client
    except HTTPException as e:
        raise e
