from pydantic import BaseModel

class Usuario(BaseModel):
    username: str
    password: str

class UsuarioCreate(BaseModel):
    username:str
    