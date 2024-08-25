from pydantic import BaseModel

class ContaCreate(BaseModel):
    cpf: str
    saldo_inicial: float
