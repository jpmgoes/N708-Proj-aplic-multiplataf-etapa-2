from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Depends, HTTPException, status
from .auth import get_current_user  # Importa a função de autenticação

app = FastAPI()

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    # Retorna as informações do usuário autenticado
    return {"username": current_user.username}


class User(BaseModel):
    id: int
    name: str
    email: str

users_db = []

@app.post("/users")
def create_user(user: User):
    users_db.append(user)
    return user


models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Authentication Service!"}