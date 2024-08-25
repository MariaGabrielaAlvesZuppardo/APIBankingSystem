from fastapi import APIRouter, Depends
from app.core.security import get_current_user
from app.api.models.usuario import UsuarioDB

router = APIRouter()

@router.get("/protected")
def protected_route(current_user: UsuarioDB = Depends(get_current_user)):
    return {"message": f"Hello {current_user.username}"}
