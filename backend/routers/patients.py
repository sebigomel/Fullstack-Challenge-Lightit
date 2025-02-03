from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.Patient import *
from ..controllers.Patient import create_patient, get_patients

router = APIRouter(prefix="/patients", tags=["patients"])

@router.post("/", response_model=PatientResponse)
def create_patient_route(patient: PatientCreate, db: Session = Depends(get_db)):
    return create_patient(db, patient)

@router.get("/", response_model=list[PatientResponse])
def get_patients_route(db: Session = Depends(get_db)):
    return get_patients(db)