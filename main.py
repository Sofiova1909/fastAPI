from fastapi import FastAPI , HTTPException
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar

app =  FastAPI()





lista_clientes: list[Cliente] = []



#endpoint para listar todos los clientes
@app.get("/clientes", response_model=list[Cliente])
async def listar_clientes():
    return lista_clientes


#endpoint para listar un solo cleinte de la lista
@app.get("/clientes/{cliente_id}", response_model=Cliente)
async def listar_cliente(cliente_id: int):
    #recorrer la lista_clientes
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            return obj_cliente
   
 
#enpoint crear_clientes
@app.post("/clientes",  response_model=Cliente)
async def crear_cliente(datos_cliente: ClienteCrear):
    cliente_val =Cliente.model_validate(datos_cliente.model_dump())
    #generar id
    len(lista_clientes)+1
    id_cliente = len(lista_clientes) + 1
    cliente_val.id = id_cliente
    lista_clientes.append(cliente_val)
    return cliente_val


#enpoint editar un cliente
@app.patch("/clientes/{cliente_id}",  response_model=Cliente)
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
    
