from sqlalchemy import Column, Integer, String
from ..database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    address = Column(String(100), nullable=False)
    phoneNum = Column(String(10), nullable=False)
    imgPath = Column(String(200), nullable=True)