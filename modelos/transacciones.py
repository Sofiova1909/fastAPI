from pydantic import BaseModel

class TransaccionBase (BaseModel):
    cantidad: int
    vr_unitario: float
    

class TransaccionCrear(TransaccionBase):
    pass

class TransaccionEditar(TransaccionBase):
    pass


class Transaccion(TransaccionBase):
    id: int | None = None
    factura_id: int | None = None  # relacion con el modelo factura (solo un campo)
# relacion con el modelo factura (solo un campo)