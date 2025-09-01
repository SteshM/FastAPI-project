# schemas.py
from uuid import UUID
from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    age: int
    grade: str
    regNo: str

class StudentUpdate(BaseModel):
    name: str
    age: int
    grade: str
    regNo: str

class StudentResponse(BaseModel):
    id: UUID
    name: str
    age: int
    grade: str
    regNo: str

    class Config:
        # Use 'from_attributes' for Pydantic v2 compatibility
        from_attributes = True

  