from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MercadoriaBase(BaseModel):
    nota_fiscal: str
    numero_serie: str
    modelo: str
    descricao: Optional[str] = None
    configurado: bool = False
    entregue: bool = False
    responsavel: str

class MercadoriaCreate(MercadoriaBase):
    pass

class MercadoriaUpdate(BaseModel):
    nota_fiscal: Optional[str] = None
    numero_serie: Optional[str] = None
    modelo: Optional[str] = None
    descricao: Optional[str] = None
    configurado: Optional[bool] = None
    entregue: Optional[bool] = None
    responsavel: Optional[str] = None

class Mercadoria(MercadoriaBase):
    id:int
    data_entrada: datetime

    class Config:
        from_attributes = True