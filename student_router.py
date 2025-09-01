# student_router.py
from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID
import services
from schemas import StudentCreate, StudentResponse, StudentUpdate

router = APIRouter(
    prefix="/students",
    tags=["students"]
)

@router.post("/", response_model=StudentResponse)
def create_student_endpoint(student: StudentCreate):
    return services.create_student(
        name=student.name,
        age=student.age,
        grade=student.grade,
        regNo=student.regNo
    )
@router.get("/students/deleted")
def get_deleted_students():
    return services.get_all_students(active_only=False, deleted_only=True)

@router.get("/{student_id}", response_model=StudentResponse)
def get_student_endpoint(student_id: UUID):
    return services.get_student(student_id)


@router.put("/{student_id}", response_model=StudentResponse)
def update_student_endpoint(student_id: UUID, student: StudentUpdate):
    return services.update_student(
        student_id,
        name=student.name,
        age=student.age,
        grade=student.grade,
        regNo=student.regNo
    )


@router.delete("/{student_id}")
def delete_student_endpoint(student_id: UUID):
    services.delete_student(student_id)
    return {"detail": "Student deleted successfully"}
