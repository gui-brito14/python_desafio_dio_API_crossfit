from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models, schemas
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

async def get_atletas(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(models.Atleta).offset(skip).limit(limit))
    return result.scalars().all()

async def create_atleta(db: AsyncSession, atleta: schemas.AtletaCreate):
    db_atleta = models.Atleta(**atleta.dict())
    db.add(db_atleta)
    try:
        await db.commit()
        await db.refresh(db_atleta)
        return db_atleta
    except IntegrityError:
        await db.rollback()
        raise HTTPException(status_code=303, detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}")
