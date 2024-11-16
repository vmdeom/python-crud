from typing import Optional
from sqlmodel import Field, SQLModel

class Produto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, nullable=True, primary_key=True)
    tipo: str
    nome: str
    codigo: str = Field(unique=True)
    preco: float
    quantidade: int