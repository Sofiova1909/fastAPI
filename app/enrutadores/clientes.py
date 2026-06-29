from http.client import HTTPException
from fastapi import APIRouter, status
from ..modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from ..listas import lista_clientes
from ..conexion_bd import sesion_dependencia
from sqlmodel import select


rutas_clientes = APIRouter()
#lista_clientes: list[Cliente] = []




#Endpoint para listar todos los clientes
@rutas_clientes.get("/clientes", response_model=list[Cliente])
async def listar_clientes(sesion: sesion_dependencia):
    lista_cli = sesion.exec(select(Cliente)).all()
    return lista_cli




#Endpoint para listar un solo cleinte de la lista
@rutas_clientes.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int, mi_sesion: sesion_dependencia):
    cliente_bd = mi_sesion.get(Cliente, cliente_id )
    if not cliente_bd:
        raise HTTPException(
        status_code=404, detail=f"El cliente con id {cliente_id}, no existe."
    )
    return cliente_bd



#Enpoint crear_clientes
@rutas_clientes.post("/clientes",  response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear, mi_sesion: sesion_dependencia):
    cliente_val =Cliente.model_validate(datos_cliente.model_dump())
    mi_sesion.add(cliente_val)
    mi_sesion.commit() #guardar cambios
    mi_sesion.refresh(cliente_val) #actualizar el objeto con los datos de la bd
    return cliente_val




#ENPOINT DE EDITAR CLIENTE Y AGREGAR A LA LISTA
@rutas_clientes.patch("/clientes/{cliente_id}",  response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: ClienteEditar, mi_sesion: sesion_dependencia):
    cliente_bd = mi_sesion.get(Cliente, cliente_id ) #buscar un cliente
    if not cliente_bd: #si no exite bota error
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail=f"El cliente con id {cliente_id}, no existe."
    )
    cliente_dict = datos_cliente.model_dump(exclude_unset=True)#convertir los datos enviados a un diaccionario de python
    cliente_bd.sqlmodel_update(cliente_dict)
    mi_sesion.add(cliente_bd)
    mi_sesion.commit() 
    mi_sesion.refresh(cliente_bd) 
    return cliente_bd




#ENDPOINT DE ELIMINAR CLIENTE
@rutas_clientes.delete("/clientes/{cliente_id}",  response_model=Cliente)
async def eliminar_cliente(cliente_id: int, mi_sesion: sesion_dependencia):
    cliente_bd = mi_sesion.get(Cliente, cliente_id )
    if not cliente_bd:
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail=f"El cliente con id {cliente_id}, no existe."
    )
    mi_sesion.delete(cliente_bd)
    mi_sesion.commit()
    return cliente_bd