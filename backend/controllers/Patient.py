from sqlalchemy.orm import Session
from ..models.Patient import Patient
from ..schemas.Patient import PatientCreate

def create_patient(db: Session, patient: PatientCreate):
    db_user = Patient(name=patient.name, email=patient.email, address=patient.address, phoneNum=patient.phoneNum, imgPath=patient.imgPath)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_patients(db: Session):
    return db.query(Patient).all()
