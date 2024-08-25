from pydantic import BaseModel
from typing import Dict

class CategoriaRelatorio(BaseModel):
    categoria: str
    total: float

class ExtratoCategoriaResponse(BaseModel):
    categorias: Dict[str, float]
