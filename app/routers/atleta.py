from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from fastapi_pagination import Page, paginate
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter()

@router.get("/atletas/", response_model=Page[schemas.Atleta])
async def read_atletas(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    atletas = await crud.get_atletas(db, skip=skip, limit=limit)
    return paginate(atletas)

@router.post("/atletas/", response_model=schemas.Atleta)
async def create_atleta(atleta: schemas.AtletaCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_atleta(db=db, atleta=atleta)
