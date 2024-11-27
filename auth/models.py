from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from .database import Base 

# Define o "Base" para o modelo de dados
Base = declarative_base()

# Configuração do banco de dados
DATABASE_URL = "postgresql://postgres:password@localhost/dbname"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # Para SQLite, ajuste conforme seu banco

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
