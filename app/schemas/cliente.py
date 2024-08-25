from pydantic import BaseModel

class ClientCreate(BaseModel):
    name: str
    date_of_birth: str
    cpf: str
    address: str
