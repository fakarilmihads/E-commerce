from pydantic import BaseModel
from enum import Enum

class RoleEnum(str, Enum):
    Penjual = 'Penjual'
    Pembeli = 'Pembeli'

class UserBase(BaseModel):
    nama: str
    email: str
    alamat: str
    nomor_hp: str | None = None
    role: RoleEnum

class UserCreate(UserBase):
    password: str

class User(UserBase):
    user_id: int

    class Config:
        orm_mode = True
