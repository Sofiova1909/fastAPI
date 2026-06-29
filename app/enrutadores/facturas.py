from http.client import HTTPException
from fastapi import APIRouter, status
from ..modelos.facturas import Factura, FacturaCrear, FacturaEditar
from ..modelos.clientes import Cliente
from ..listas import lista_clientes, lista_facturas
from ..conexion_bd import sesion_dependencia
from sqlmodel import select
rutas_facturas = APIRouter()

#lista_clientes: list[Cliente] = []
#lista_facturas: list[Factura] = []

#ENDPOINTS DE FACTURAS

@rutas_facturas.get("/facturas", response_model=list[Factura])
async def listar_facturas(sesion: sesion_dependencia):
    consulta = select(Factura)
    lista_facturas = sesion.exec(consulta).all()
    return listar_facturas


@rutas_facturas.get("/facturas/{factura_id}", response_model=Factura)
async def listar_facturas(factura_id: int):
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
async def editar_facturas(factura_id: int, datos_factura: Factura):
    pass

@rutas_facturas.delete("/facturas/{id_factura}", response_model=list[Factura])
async def eliminar_facturas(id_factura):
    pass
