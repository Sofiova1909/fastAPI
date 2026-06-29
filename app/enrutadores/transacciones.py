from fastapi import APIRouter, HTTPException, status
from ..modelos.facturas import Factura #..modelos.facturas --> salir de la carpeta factura, entrar en la carpeta modelos, y mostrar el archivo factura
from ..modelos.transacciones import Transaccion, TransaccionCrear, TransaccionEditar
from ..listas import lista_clientes, lista_facturas, lista_transacciones
from ..conexion_bd import sesion_dependencia
from sqlmodel import select


rutas_transacciones = APIRouter()


#lista_facturas: list[Factura] = []
#lista_transacciones: list[Transaccion] = []

#Crear los Enpoints de Transacciones

@rutas_transacciones.get("/transacciones", response_model=list[Transaccion])
async def listar_transacciones(sesion:sesion_dependencia ):
    # consulta = select(Transaccion)
    #lista_transacciones = sesion.exec(consulta).all()
    #return lista_transacciones
    return sesion.exec(select(Transaccion)).all() #resumido en una linea las lineas 19 -21



@rutas_transacciones.get("/transacciones/{id_transaccion}", response_model=Transaccion)
async def listar_transacciones(id_transaccion: int):
    pass



@rutas_transacciones.post("/transacciones/{factura_id}", response_model=Transaccion)
async def crear_transacciones(factura_id: int, datos_transaccion: TransaccionCrear, sesion: sesion_dependencia):
    #buscar una factura
    factura_encontrada = sesion.get(Factura, factura_id)
    #si no existe la factura
    if not factura_encontrada:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"La factura con id {factura_id}, no existe."
        )



    #validar datos de la transaccion -json  a dict 
    transaccion_dict = datos_transaccion.model_dump()
    transaccion_dict["factura_id"] = factura_id
    transaccion_val = Transaccion.model_validate(transaccion_dict)
    #guardar en bd
    sesion.add(transaccion_val)
    sesion.commit()
    sesion.refresh(transaccion_val)
    return transaccion_val



@rutas_transacciones.patch("/transacciones/{id_transaccion}", response_model=Transaccion)
async def editar_transaccion(id_factura: int, datos_transaccion: Transaccion):
    pass


@rutas_transacciones.delete("/transacciones/{id_transaccion}", response_model=Transaccion)
async def eliminar_transaccion(id_transaccion: int):
    pass