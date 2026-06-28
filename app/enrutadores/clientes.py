from http.client import HTTPException
from fastapi import APIRouter
from ..modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from ..listas import lista_clientes
from ..conexion_bd import sesion_dependencia


rutas_clientes = APIRouter()
#lista_clientes: list[Cliente] = []

#Endpoint para listar todos los clientes
@rutas_clientes.get("/clientes", response_model=list[Cliente])
async def listar_clientes():
    return lista_clientes


#Endpoint para listar un solo cleinte de la lista
@rutas_clientes.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int, mi_sesion: sesion_dependencia):
    #recorrer la lista_clientes
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            return obj_cliente
    raise HTTPException(
        status_code=404, detail=f"El cliente con id {cliente_id}, no existe."
    )

#Enpoint crear_clientes
@rutas_clientes.post("/clientes",  response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear, mi_sesion: sesion_dependencia):
    cliente_val =Cliente.model_validate(datos_cliente.model_dump())
    mi_sesion.add(cliente_val)
    mi_sesion.commit() #guardar cambios
    mi_sesion.refresh(cliente_val) #actualizar el objeto con los datos de la bd
    return cliente_val


#Enpoint editar un cliente
@rutas_clientes.patch("/clientes/{cliente_id}",  response_model=Cliente)
async def editar_cliente(cliente_id: int, datos_cliente: ClienteEditar):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            #validar cliente
            cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            cliente_val.id = cliente_id
            lista_clientes[i] = cliente_val
            return obj_cliente
    raise HTTPException(
        status_code=404, detail=f"El cliente con id {cliente_id}, no existe."
        )

#Enpoint eliminar cliente
@rutas_clientes.delete("/clientes/{cliente_id}",  response_model=Cliente)
async def eliminar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            cliente_eliminado = lista_clientes.pop(i)
            return cliente_eliminado
    raise HTTPException(
        status_code=404, detail=f"El cliente con id {cliente_id}, no existe."
        )