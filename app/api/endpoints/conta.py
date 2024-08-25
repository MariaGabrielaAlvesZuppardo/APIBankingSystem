

from fastapi import APIRouter, HTTPException, Depends
from app.schemas.conta_update import ContaUpdate
from app.services.banco_service import BancoService

router = APIRouter()

def get_banco_service():
    return BancoService()

@router.put("/{numero}")
def update_conta(numero: int, conta_update: ContaUpdate, banco_service: BancoService = Depends(get_banco_service)):
    try:
        conta = banco_service.buscar_conta_por_numero(numero)
        if not conta:
            raise HTTPException(status_code=404, detail="Conta não encontrada.")
        
        if conta_update.endereco:
            conta.endereco = conta_update.endereco
        if conta_update.telefone:
            conta.telefone = conta_update.telefone
        
        return conta
    except HTTPException as e:
        raise e
    
    
@router.delete("/{numero}")
def delete_conta(numero: int, banco_service: BancoService = Depends(get_banco_service)):
    try:
        conta = banco_service.buscar_conta_por_numero(numero)
        if not conta:
            raise HTTPException(status_code=404, detail="Conta não encontrada.")
        
        banco_service.encerrar_conta(numero)
        return {"message": "Conta encerrada com sucesso."}
    except HTTPException as e:
        raise e