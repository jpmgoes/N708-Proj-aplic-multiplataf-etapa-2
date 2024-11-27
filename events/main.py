from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi import Depends, HTTPException, status
from .auth import get_current_user  # Importa a função de autenticação

app = FastAPI()

@app.get("/events")
async def get_events(current_user: User = Depends(get_current_user)):
    # A lógica de obter eventos vai aqui
    return {"message": "Eventos listados com sucesso", "user": current_user.username}

class Event(BaseModel):
    id: int
    title: str
    description: str
    date: str
    organizer: str

events_db: List[Event] = []

@app.post("/events")
def create_event(event: Event):
    events_db.append(event)
    return {"message": "Event created successfully", "event": event}

@app.get("/events")
def list_events():
    return events_db

@app.delete("/events/{event_id}")
def delete_event(event_id: int):
    global events_db
    events_db = [event for event in events_db if event.id != event_id]
    return {"message": "Event deleted successfully"}

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Authentication Service!"}

