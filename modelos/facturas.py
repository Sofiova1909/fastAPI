from pydantic import BaseModel, computed_field

from .transacciones import Transaccion
from .clientes import Cliente
from datetime import datetime


class FacturaBase(BaseModel):
    fecha: str = datetime.now()
    cliente: Cliente #relaicon entre cliente(objeto)
    transacciones: list[Transaccion] = [] #relacion entre transacciones (lista de diccionarios)


    @computed_field
    @property
    def vr_total(self) -> float:
        #calcular (cantidad * vr_unitario) 
        #consultar el id actual de la factura
        factura_id_actual = getattr(self, "id", None)
        total_factura = 0.0
        if not factura_id_actual or not self.transacciones:
            return total_factura
        #Recorrer la lista de transacciones egun el id de factura
        for transaccion  in self.transacciones:
            if transaccion.factura_id == factura_id_actual:
                total_factura += transaccion.vr_unitario * transaccion.cantidad
        return 222



class FacturaCrear(FacturaBase):
    pass

class FacturaEditar(FacturaBase):
    pass

class Factura(FacturaBase):
    id: int | None = None