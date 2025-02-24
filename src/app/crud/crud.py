from sqlalchemy.orm import Session
from ..models import models
from ..schemas import schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(nama=user.nama, email=user.email, password=user.password, alamat=user.alamat, nomor_hp=user.nomor_hp, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
