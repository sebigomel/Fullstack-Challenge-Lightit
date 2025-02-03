from fastapi import FastAPI
from .routers import patients
from .database import Base, engine

Base.metadata.create_all(bind=engine) 

app = FastAPI(title="FastAPI + MySQL Docker Example")

app.include_router(patients.router)
