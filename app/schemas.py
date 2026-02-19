from typing import Optional
from pydantic import BaseModel, Field

# BaseModel es la clase base de Pydantic.
# Al heredar de ella, tu clase obtiene validación automática.
class Tarea(BaseModel):
    titulo: str                         # obligatorio, debe ser texto
    descripcion: Optional[str] = None   # opcional, por defecto None
    completada: bool = False            # opcional, por defecto False
    prioridad: int = 1                  # opcional, por defecto 1
    
class Usuario(BaseModel):
    nombre: str = Field(min_length=2, max_length=50)
    email: str = Field(pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    edad: Optional[int] = Field(default=None, ge=0, le=120)
    activo: bool = True
    
