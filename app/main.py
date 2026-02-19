from fastapi import FastAPI
from app.schemas import Tarea

app = FastAPI(title="TaskMaster API", version="0.1.0")

@app.get("/health")
def health_check():
    return {"status": "ok"}

# POST /tareas — recibe un JSON, lo valida con Pydantic, lo devuelve
@app.post("/tareas")
def crear_tarea(tarea: Tarea):
    return tarea