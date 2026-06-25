from fastapi import FastAPI , HTTPException
from modelos.clientes import Cliente, ClienteCrear, ClienteEditar
from modelos.facturas import Factura, FacturaCrear, FacturaEditar
from modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar

app =  FastAPI()





lista_clientes: list[Cliente] = []
lista_facturas: list[Factura] = []
lista_transacciones: list[Transaccion] = []



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

#enpoint eliminar cliente
@app.delete("/clientes/{cliente_id}",  response_model=Cliente)
async def eliminar_cliente(cliente_id: int):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == cliente_id:
            cliente_eliminado = lista_clientes.pop(i)
            return cliente_eliminado
    raise HTTPException(
        status_code=404, detail=f"El cliente con id {cliente_id}, no existe."
        )



#Enpoinds de facturas
@app.get("/facturas", response_model=list[Factura])
async def listar_facturas():
    return listar_facturas

@app.get("/facturas/{id_factura}", response_model=list[Factura])
async def listar_facturas(id_factura: int):
    pass

@app.post("/facturas/{id_cliente}", response_model=Factura)
async def crear_facturas(id_cliente: int, datos_factura: Factura):
    pass

@app.patch("/facturas/{id_factura}", response_model=Factura)
async def editar_facturas(id_factura: int, datos_factura: Factura):
    pass

@app.delete("/facturas/{id_factura}", response_model=list[Factura])
async def eliminar_facturas(id_factura):
    pass

