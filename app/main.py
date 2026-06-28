from fastapi import FastAPI , HTTPException, status
from app.enrutadores.clientes import rutas_clientes
from app.enrutadores.facturas import rutas_facturas
from app.enrutadores.transacciones import rutas_transacciones
from app.conexion_bd import crear_tablas


app =  FastAPI(lifespan=crear_tablas)



#Ruta de clientes
app.include_router(rutas_clientes, tags=["Clientes"])

#Ruta de facturas
app.include_router(rutas_facturas, tags=["Facturas"])

#Ruta de transacciones
app.include_router(rutas_transacciones, tags=["Transacciones"])



