from pydantic import BaseModel, EmailStr, Field

class PatientBase(BaseModel):
    name: str =  Field(title="Nombre", description="Solo letras y espacios", min_length=1, max_length=100, pattern="^[a-zA-Z ]+$")
    email: EmailStr  = Field(title="Correo", description="Correo electronico", min_length=1, max_length=100, pattern="^[a-zA-Z0-9._%+-]+@gmail\.com$")
    address: str
    phoneNum: str = Field(title="Telefono", description="Solo numeros", min_length=1, max_length=10, pattern="^[0-9]+$")
    imgPath: str

class PatientCreate(PatientBase):
    pass

class PatientResponse(PatientBase):
    id: int
    class Config:
        from_attributes = True
