from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.api.models.usuario import UsuarioDB
from app.core.banco import Banco

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Mock Banco instance for user validation
banco = Banco()  # Replace with your actual database connection or singleton instance

def get_current_user(token: str = Depends(oauth2_scheme)) -> UsuarioDB:
    user = banco.find_user_by_username(token)  # Replace token with actual user validation logic
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user
