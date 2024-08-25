from pydantic import BaseModel

class AccountCreate(BaseModel):
    cpf: str
    initial_balance: float
