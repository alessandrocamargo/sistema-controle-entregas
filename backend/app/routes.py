from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from . import crud, schemas, database
from .models import Mercadoria

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/mercadorias/", response_model=schemas.Mercadoria, status_code=status.HTTP_201_CREATED)
def create_mercadoria(mercadoria: schemas.MercadoriaCreate, db: Session = Depends(get_db)):
    # Verificar se número de série já existe
    existing = db.query(Mercadoria).filter(
        Mercadoria.numero_serie == mercadoria.numero_serie
    ).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Número de série já cadastrado"
        )
    return crud.create_mercadoria(db=db, mercadoria=mercadoria)

@router.get("/mercadorias/", response_model=List[schemas.Mercadoria])
def read_mercadorias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    mercadorias = crud.get_mercadorias(db, skip=skip, limit=limit)
    return mercadorias

@router.get("/mercadorias/{mercadoria_id}", response_model=schemas.Mercadoria)
def read_mercadoria(mercadoria_id: int, db: Session = Depends(get_db)):
    db_mercadoria = crud.get_mercadoria(db, mercadoria_id)
    if db_mercadoria is None:
        raise HTTPException(status_code=404, detail="Mercadoria não encontrada")
    return db_mercadoria

@router.put("/mercadorias/{mercadoria_id}", response_model=schemas.Mercadoria)
def update_mercadoria(mercadoria_id: int, mercadoria: schemas.MercadoriaUpdate, db: Session = Depends(get_db)):
    db_mercadoria = crud.update_mercadoria(db, mercadoria_id, mercadoria)
    if db_mercadoria is None:
        raise HTTPException(status_code=404, detail="Mercadoria não encontrada")
    return db_mercadoria

@router.delete("/mercadorias/{mercadoria_id}")
def delete_mercadoria(mercadoria_id: int, db: Session = Depends(get_db)):
    success = crud.delete_mercadoria(db, mercadoria_id)
    if not success:
        raise HTTPException(status_code=404, detail="Mercadoria não encontrada")
    return {"message": "Mercadoria deletada com sucesso"}

@router.get("/relatorios/nao-entregues/", response_model=List[schemas.Mercadoria])
def relatorio_nao_entregues(db: Session = Depends(get_db)):
    return crud.get_mercadorias_nao_entregues(db)