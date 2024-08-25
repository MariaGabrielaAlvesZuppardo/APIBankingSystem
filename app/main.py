from fastapi import FastAPI
from app.core.db import engine
from app.core.init_db import init_db

app = FastAPI()

# Inicializa o banco de dados na inicialização do aplicativo
@app.on_event("startup")
async def on_startup():
    await init_db()

# Inclua suas rotas
from app.api.endpoints import auth, cliente, conta, transacao
app.include_router(auth.router, prefix="/auth")
app.include_router(cliente.router, prefix="/clientes")
app.include_router(conta.router, prefix="/contas")
app.include_router(transacao.router, prefix="/transacoes")

