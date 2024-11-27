from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# URL de conexão com o PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost/postgres")

# Criar engine para o banco de dados
engine = create_engine(DATABASE_URL)

# Base para os modelos
Base = declarative_base()

# Criar sessão para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para obter a sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
