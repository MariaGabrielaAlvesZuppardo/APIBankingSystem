from pydantic import BaseModel

class ClienteCreate(BaseModel):
    nome: str
    data_nascimento: str
    cpf: str
    endereco: str
