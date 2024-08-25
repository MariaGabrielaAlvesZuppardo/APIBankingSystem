from fastapi import FastAPI
from app.api.endpoints import cliente, conta, transacao, extrato

app = FastAPI()

app.include_router(cliente.router, prefix="/clientes", tags=["clientes"])
app.include_router(conta.router, prefix="/contas", tags=["contas"])
app.include_router(transacao.router, prefix="/transacoes", tags=["transacoes"])
app.include_router(extrato.router, prefix="/extratos", tags=["extratos"])
