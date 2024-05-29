from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.security.http import HTTPAuthorizationCredentials
from pydantic import BaseModel, Field
from typing import Coroutine, Optional, List
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer

app = FastAPI(
    title = "Uso de JWT",
    version= "1.0.0"
)

class Usuario(BaseModel):
    correo: str
    password: str = Field(min_length=4)

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@example.com":
            raise(HTTPException(status_code=403, detail="Credenciales invalidas"))

@app.get("/", tags=["Home"])
def home():
    return HTMLResponse("<h1>Usando JWT con fast API</h1>")

@app.post("/login", tags=["autheticator"])
async def login(user:Usuario):
    if(user.correo=="admin@example.com" and user.password=="1234"):
        return JSONResponse(content=create_token(user.dict()), status_code=200)
    else:
        return JSONResponse(content="Error en autenticación", status_code=400)
    
@app.get("/data", tags=["Datos"])
async def get_data():
    return JSONResponse(content={"message":"contenido"}, status_code=200) 