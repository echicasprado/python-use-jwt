from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import create_token

app = FastAPI(
    title = "Uso de JWT",
    version= "1.0.0"
)

class Usuario(BaseModel):
    correo: str
    password: str = Field(min_length=4)

@app.get("/", tags=["Home"])
def home():
    return HTMLResponse("<h1>Usando JWT con fast API</h1>")

@app.post("/login", tags=["autheticator"])
async def login(user:Usuario):
    if(user.correo=="admin@example.com" and user.password=="1234"):
        return JSONResponse(content=create_token(user.dict()), status_code=200)
    else:
        return JSONResponse(content="Error en autenticación", status_code=400)