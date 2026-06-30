from pydantic import BaseModel, computed_field
from sqlmodel import SQLModel, Field, Relationship
from .transacciones import Transaccion
from .clientes import Cliente, ClienteLeer
from datetime import datetime

class FacturaBase(SQLModel):
    fecha: datetime = Field(default_factory=datetime.now)
    #cliente: Cliente #relaicon entre cliente(objeto)
    #transacciones: list[Transaccion] = [] #relacion entre transacciones (lista de diccionarios)

    @computed_field
    @property
    def vr_total(self) -> float:
        total_factura = 0.0
        if self.transacciones == None:
            return total_factura
        #Recorrer la lista de transacciones egun el id de factura
        for transaccion  in self.transacciones:
            total_factura += transaccion.vr_unitario * transaccion.cantidad
        return total_factura



class FacturaCrear(FacturaBase):
    pass


class FacturaEditar(FacturaBase):
    pass


class Factura(FacturaBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cliente_id: int = Field(default=None, foreign_key="cliente.id")
    #Crear relaciones virtuales con cliente, transaccion -No en la BD
    cliente : "Cliente" = Relationship(back_populates="factura")
    transacciones: list[Transaccion] = Relationship(back_populates="factura")


#crea modelo para mostrar la usuario o el cliente
class FacturaLeer(FacturaBase):
    id: int
    cliente: ClienteLeer
    #transaccion: list[Transaccion] = []

class FacturaLeerCompuesta(FacturaLeer):
    transacciones: list[Transaccion] = []