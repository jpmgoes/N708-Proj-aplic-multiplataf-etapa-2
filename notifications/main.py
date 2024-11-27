from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi import Depends, HTTPException, status
from .auth import get_current_user  # Importa a função de autenticação

app = FastAPI()

@app.post("/notifications")
async def send_notification(message: str, current_user: User = Depends(get_current_user)):
    # Lógica para enviar a notificação
    return {"message": f"Notificação enviada para {current_user.username}"}

class Notification(BaseModel):
    id: int
    message: str
    recipient: str
    timestamp: str

notifications_db: List[Notification] = []

@app.post("/notifications")
def send_notification(notification: Notification):
    notifications_db.append(notification)
    return {"message": "Notification sent successfully"}

@app.get("/notifications")
def list_notifications():
    return notifications_db


models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Authentication Service!"}

@app.post("/notify")
def notify(message: str):
    # Enviar mensagem para a fila RabbitMQ
    publish_message(message)
    return {"message": "Notificação enviada"}

@app.get("/consume")
def consume():
    # Consumir mensagens da fila RabbitMQ
    consume_message()
    return {"message": "Consumo de mensagens iniciado"}