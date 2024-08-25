from pydantic import BaseModel

class TransactionCreate(BaseModel):
    cpf: str
    type: str
    value: float
