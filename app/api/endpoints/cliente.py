from fastapi import APIRouter, HTTPException
from app.schemas.cliente import ClienteCreate 
from app.services.banco_service import BancoService 

router = APIRouter ()
banco_service = BancoService ()

@router.post("/")
def create_cliente(cliente_create: ClienteCreate):
    try:
        cliente = banco_service.cadastrar_cliente(cliente_create.nome,cliente_create.data_nascimento,cliente_create.cpf,cliente_create.endereco)
        return cliente 
    except HTTPException as e:
        raise e