from pydantic import BaseModel
from typing import Optional

class CategoriaBase(BaseModel):
    nome: str

class CategoriaCreate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    id: str

    class Config:
        orm_mode = True

class CentroTreinamentoBase(BaseModel):
    nome: str
    endereco: str
    proprietario: str

class CentroTreinamentoCreate(CentroTreinamentoBase):
    pass

class CentroTreinamento(CentroTreinamentoBase):
    id: str

    class Config:
        orm_mode = True

class AtletaBase(BaseModel):
    nome: str
    cpf: str
    idade: int
    peso: float
    altura: float
    sexo: str

class AtletaCreate(AtletaBase):
    centro_treinamento_id: int
    categoria_id: int

class Atleta(AtletaBase):
    id: str
    centro_treinamento: CentroTreinamento
    categoria: Categoria

    class Config:
        orm_mode = True
