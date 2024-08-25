from fastapi import APIRouter, HTTPException, Depends
from app.schemas.cliente import ClienteCreate
from app.services.banco_service import BancoService

router = APIRouter()

def get_banco_service():
    return BancoService()

@router.post("/clientes/")
def create_cliente(cliente_create: ClienteCreate, banco_service: BancoService = Depends(get_banco_service)):
    try:
        cliente = banco_service.cadastrar_cliente(
            cliente_create.nome,
            cliente_create.data_nascimento,
            cliente_create.cpf,
            cliente_create.endereco
        )
        if not cliente:
            raise HTTPException(status_code=400, detail="Client already registered.")
        return cliente
    except HTTPException as e:
        raise e
