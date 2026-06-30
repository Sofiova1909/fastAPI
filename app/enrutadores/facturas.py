from fastapi import APIRouter, HTTPException, status
from ..modelos.facturas import Factura, FacturaCrear, FacturaEditar, FacturaLeer, FacturaLeerCompuesta
from ..modelos.clientes import Cliente
from ..listas import lista_clientes, lista_facturas
from ..conexion_bd import sesion_dependencia
from sqlmodel import select
rutas_facturas = APIRouter()

#lista_clientes: list[Cliente] = []
#lista_facturas: list[Factura] = []

#ENDPOINTS DE FACTURAS

@rutas_facturas.get("/facturas", response_model=list[FacturaLeerCompuesta])
async def listar_facturas(sesion: sesion_dependencia):
    consulta = select(Factura)
    lista_facturas = sesion.exec(consulta).all()
    return lista_facturas


@rutas_facturas.get("/facturas/{factura_id}", response_model=FacturaLeer)
async def listar_factura(factura_id: int, sesion: sesion_dependencia):
    factura_bd = sesion.get(Factura, factura_id)
    #recorrer la lista_facturas
    for i, obj_factura in enumerate(lista_facturas):
        if obj_factura.id == factura_id:
            return obj_factura
    raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"La factura con id {factura_id}, no existe."
    )



@rutas_facturas.post("/facturas/{cliente_id}", response_model=Factura)
async def crear_facturas(cliente_id: int, datos_factura: FacturaCrear, sesion: sesion_dependencia):
    #buscar el cliente en bd

    cliente_encontrado = sesion.get(Cliente, cliente_id)
    #mensaje si no existe el cliente
    if not cliente_encontrado:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"El cliente con id {cliente_id}, no existe."
        )

    #validar datos de la factura-json, pasar dict
    factura_dict = datos_factura.model_dump()
    factura_dict["cliente_id"] = cliente_id
    factura_val = Factura.model_validate(factura_dict)
    #guardar en bd
    sesion.add(factura_val)
    sesion.commit ()
    sesion.refresh(factura_val)
    return factura_val



@rutas_facturas.patch("/facturas/{factura_id}", response_model=Factura)
async def editar_facturas(factura_id: int, datos_factura: FacturaEditar, sesion: sesion_dependencia):
    factura_bd = sesion.get(Factura, factura_id ) #buscar una factura
    if not factura_bd: #si no exite bota error
        raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail=f"La factura con id {factura_id}, no existe."
    )
    factura_dict = datos_factura.model_dump(exclude_unset=True)#convertir los datos enviados a un diaccionario de python
    factura_bd.sqlmodel_update(factura_dict)
    sesion.add(factura_bd)
    sesion.commit() 
    sesion.refresh(factura_bd) 
    return factura_bd




@rutas_facturas.delete("/facturas/{factura_id}", response_model=Factura)
async def eliminar_facturas(factura_id: int, sesion: sesion_dependencia):

    factura_bd = sesion.get(Factura, factura_id)

    if not factura_bd:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"La factura con id {factura_id} no existe."
        )

    sesion.delete(factura_bd)
    sesion.commit()

    return factura_bd
