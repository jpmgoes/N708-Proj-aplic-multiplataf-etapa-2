from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi import Depends, HTTPException, status
from .auth import get_current_user  # Importa a função de autenticação

app = FastAPI()

@app.patch("/resources/{resource_id}")
async def update_resource(resource_id: int, availability: bool, current_user: User = Depends(get_current_user)):
    # Aqui você pode adicionar a lógica para alterar a disponibilidade de um recurso
    return {"message": f"Recurso {resource_id} atualizado", "user": current_user.username}

class Resource(BaseModel):
    id: int
    name: str
    type: str
    availability: bool

resources_db: List[Resource] = []

@app.post("/resources")
def add_resource(resource: Resource):
    resources_db.append(resource)
    return {"message": "Resource added successfully", "resource": resource}

@app.get("/resources")
def list_resources():
    return resources_db

@app.patch("/resources/{resource_id}")
def update_availability(resource_id: int, availability: bool):
    for resource in resources_db:
        if resource.id == resource_id:
            resource.availability = availability
            return {"message": "Resource updated successfully"}
    return {"message": "Resource not found"}


models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Authentication Service!"}
