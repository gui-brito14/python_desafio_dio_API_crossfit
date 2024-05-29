from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class Categoria(Base):
    __tablename__ = "categoria"
    pk_id = Column(Integer, primary_key=True, index=True)
    id = Column(String, default=uuid.uuid4, unique=True, index=True)
    nome = Column(String(10), unique=True)

class CentroTreinamento(Base):
    __tablename__ = "centro_treinamento"
    pk_id = Column(Integer, primary_key=True, index=True)
    id = Column(String, default=uuid.uuid4, unique=True, index=True)
    nome = Column(String(20), unique=True)
    endereco = Column(String(60))
    proprietario = Column(String(30))

class Atleta(Base):
    __tablename__ = "atleta"
    pk_id = Column(Integer, primary_key=True, index=True)
    id = Column(String, default=uuid.uuid4, unique=True, index=True)
    nome = Column(String(50))
    cpf = Column(String(11), unique=True, index=True)
    idade = Column(Integer)
    peso = Column(Float)
    altura = Column(Float)
    sexo = Column(String(1))
    centro_treinamento_id = Column(Integer, ForeignKey("centro_treinamento.pk_id"))
    categoria_id = Column(Integer, ForeignKey("categoria.pk_id"))

    centro_treinamento = relationship("CentroTreinamento")
    categoria = relationship("Categoria")
