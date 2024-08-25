from fastapi import APIRouter, HTTPException, Depends
from app.schemas.conta import ContaCreate
from app.services.banco_service import BancoService

router = APIRouter()

def get_banco_service():
    return BancoService()

@router.post("/contas/")
def create_conta(conta_create: ContaCreate, banco_service: BancoService = Depends(get_banco_service)):
    try:
        conta = banco_service.criar_conta_corrente(
            conta_create.cpf,
            conta_create.saldo_inicial
        )
        if not conta:
            raise HTTPException(status_code=400, detail="Client not found.")
        return conta
    except HTTPException as e:
        raise e
