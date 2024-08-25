# app/schemas/relatorio.py
from pydantic import BaseModel
from typing import List

class TransacaoRelatorio(BaseModel):
    data: str
    tipo: str
    valor: float

class RelatorioResponse(BaseModel):
    transacoes: List[TransacaoRelatorio]
    total: float

# app/schemas/categoria.py
from pydantic import BaseModel
from typing import Dict

class CategoriaRelatorio(BaseModel):
    categoria: str
    total: float

class ExtratoCategoriaResponse(BaseModel):
    categorias: Dict[str, float]
