from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.core.security import criar_hash_senha, verificar_senha, criar_token_acesso, verificar_token_acesso
from app.core.banco import Banco
from app.api.models.usuario import UsuarioCreate

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
banco = Banco()  # Simulação do banco de dados

@router.post("/register")
def register(usuario_create: UsuarioCreate):
    hashed_password = criar_hash_senha(usuario_create.password)
    usuario = banco.cadastrar_usuario(usuario_create.username, hashed_password)
    return {"username": usuario.username}

@router.post("/token")
def login(usuario_create: UsuarioCreate):
    usuario = banco.buscar_usuario_por_username(usuario_create.username)
    if not usuario or not verificar_senha(usuario_create.password, usuario.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = criar_token_acesso(usuario_create.username)
    return {"access_token": access_token, "token_type": "bearer"}

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401, detail="Could not validate credentials"
    )
    username = verificar_token_acesso(token, credentials_exception)
    return username
