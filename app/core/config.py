import os

# Substitua pelos detalhes do seu banco de dados PostgreSQL no Render
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://systembanking_user:pzfK9u4Knh1sZ1K1xPXeRvd92KSsMXla@localhost/systembanking"
)
