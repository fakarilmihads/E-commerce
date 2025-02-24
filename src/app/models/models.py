from sqlalchemy import Column, Integer, String, Text, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class RoleEnum(enum.Enum):
    Penjual = 'Penjual'
    Pembeli = 'Pembeli'

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nama = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    alamat = Column(Text, nullable=False)
    nomor_hp = Column(String(15))
    role = Column(Enum(RoleEnum), nullable=False)
