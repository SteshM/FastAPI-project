# services.py
from models import Student
from typing import List
from uuid import UUID
from fastapi import HTTPException

# In-memory database
students: List[Student] = []

def create_student(name: str, age: int, grade: str, regNo: str) -> Student:
    student = Student(name, age, grade, regNo)
    students.append(student)
    return student

def get_all_students(deleted: bool | None = None):
    if deleted is True:   # only deleted students
        return [s for s in students if s.deleted]
    if deleted is False:  # only active students
        return [s for s in students if not s.deleted]
    return students       # all students


def get_student(student_id: UUID) -> Student:
    for student in students:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")


def update_student(student_id: UUID, name: str, 
                   age: int, grade: str, regNo: str) -> Student:
    for student in students:
        if student.id == student_id:
            student.name = name
            student.age = age
            student.grade = grade
            student.regNo = regNo
            return student
    raise HTTPException(status_code=404, detail="Student not found")


# services.py
def delete_student(student_id: UUID):
    for student in students:
        if student.id == student_id:
            student.deleted = True  # mark as deleted instead of removing
            return
    raise HTTPException(status_code=404, detail="Student not found")

