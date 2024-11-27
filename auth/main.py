from fastapi import FastAPI, HTTPException, Depends
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer  
from passlib.context import CryptContext
from pydantic import BaseModel  
from fastapi.security import OAuth2PasswordRequestForm 
from auth import models  
from auth.database import engine  
from auth.models import Base, engine
from fastapi import FastAPI
from .models import Base, User # Importa Base de models
from .database import engine  # Importa engine de database.py


# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# OAuth2 Password Bearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Inicializar o CryptContext para o hashing de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Usuário de exemplo 
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "password": "$2b$12$NqA.K3c6gkT1hjxj6x.Ns.k.xbdqzqkmSShg7UyDhtyS6kpqu0Z7S",  # "password"
    }
}    

# Modelo para o Token
class Token(BaseModel):
    access_token: str
    token_type: str

# Modelo de usuário
class User(BaseModel):
    username: str

# Função para verificar se a senha está correta
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Função para obter usuário do banco de dados (simulado)
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return User(**user_dict)

# Função para criar um token JWT
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Rota para login (retorna o token JWT)
@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user(fake_users_db, form_data.username)
    if not user or not verify_password(form_data.password, fake_users_db[user.username]["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Função para pegar o usuário a partir do token
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return User(username=username)
    except JWTError:
        raise credentials_exception

# Rota para acessar informações de um usuário autenticado
@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.post("/token")
def login(username: str, password: str):
    if username == "admin" and password == "123":
        expiration = datetime.utcnow() + timedelta(hours=1)
        token = jwt.encode({"exp": expiration}, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Authentication Service!"}
