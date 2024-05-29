from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from jwt_manager import create_token
from models import Usuario, JWT_Bearer

app = FastAPI(
    title = "Uso de JWT",
    version= "1.0.0"
)

@app.get("/", tags=["Home"])
def home():
    return HTMLResponse("<h1>Usando JWT con fast API</h1>")

@app.post("/login", tags=["autheticator"])
async def login(user:Usuario):
    if(user.correo=="admin@example.com" and user.password=="1234"):
        return JSONResponse(content=create_token(user.dict()), status_code=200)
    else:
        return JSONResponse(content="Error en autenticación", status_code=400)
    
@app.get("/data", tags=["Datos"], dependencies=[Depends(JWT_Bearer())])
async def get_data():
    return JSONResponse(content={"message":"contenido"}, status_code=200) 