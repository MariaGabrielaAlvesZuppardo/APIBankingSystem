from pydantic import BaseModel

class TransacaoCreate(BaseModel):
    cpf: str
    tipo: str
    valor: float
