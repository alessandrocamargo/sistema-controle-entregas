from sqlalchemy.orm import Session
from . import models, schemas

def get_mercadoria(db: Session, mercadoria_id: int):
    return db.query(models.Mercadoria).filter(models.Mercadoria.id == mercadoria_id).first()

def get_mercadorias(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Mercadoria).offset(skip).limit(limit).all()

def create_mercadoria(db: Session, mercadoria: schemas.MercadoriaCreate):
    # Converter para dicionário
    mercadoria_dict = mercadoria.model_dump()
    db_mercadoria = models.Mercadoria(**mercadoria_dict)
    db.add(db_mercadoria)
    db.commit()
    db.refresh(db_mercadoria)
    return db_mercadoria

def update_mercadoria(db: Session, mercadoria_id: int, mercadoria: schemas.MercadoriaUpdate):
    db_mercadoria = get_mercadoria(db, mercadoria_id)
    if db_mercadoria:
        update_data = mercadoria.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_mercadoria, field, value)
        db.commit()
        db.refresh(db_mercadoria)
    return db_mercadoria

def delete_mercadoria(db: Session, mercadoria_id: int):
    db_mercadoria = get_mercadoria(db, mercadoria_id)
    if db_mercadoria:
        db.delete(db_mercadoria)
        db.commit()
        return True
    return False

def get_mercadorias_nao_entregues(db: Session):
    return db.query(models.Mercadoria).filter(models.Mercadoria.entregue == False).all()