
from pydantic import BaseModel 

#Crear modelo clientes (id, nombre, email, descirpcion)
class ClienteBase(BaseModel):
    nombre: str
    email:str
    descripcion: str


class ClienteCrear(ClienteBase):
    pass

class ClienteEditar(ClienteBase):
    pass



class Cliente(ClienteBase):
    id: int | None = None