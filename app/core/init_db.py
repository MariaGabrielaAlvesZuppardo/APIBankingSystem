from app.core.db import engine
from app.api.models import cliente, conta

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(cliente.Base.metadata.create_all)
        await conn.run_sync(conta.Base.metadata.create_all)
