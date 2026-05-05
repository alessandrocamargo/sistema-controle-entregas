from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.sql import func
from .database import Base

class Mercadoria(Base):
    __tablename__ = "mercadorias"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nota_fiscal = Column(String(50), nullable=False, index=True)
    numero_serie = Column(String(100), nullable=False, unique=True, index=True)
    modelo = Column(String(100), nullable=False)
    descricao = Column(Text, nullable=True)
    configurado = Column(Boolean, default=False)
    entregue = Column(Boolean, default=False)
    responsavel = Column(String(100), nullable=False)
    data_entrada = Column(DateTime, server_default=func.now(), nullable=False)

    def __repr__(self):
        return f"<Mercadoria {self.numero_serie}>"