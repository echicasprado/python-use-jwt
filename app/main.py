from fastapi import FastAPI, body, Path, Query
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
