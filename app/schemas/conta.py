from pydantic import BaseModel

class AccountCreate(BaseModel):
    cpf: str
    initial_balance: float
    endereco: Optional[str] = Field(None, example="Rua A, 123 - Bairro B - Cidade C - SP")
    telefone: Optional[str] = Field(None, example="11987654321")
