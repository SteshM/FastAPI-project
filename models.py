
# models.py
from uuid import uuid4, UUID

class Student:
    def __init__(self, name: str, age: int, grade: str, regNo: str):
        self.id: UUID = uuid4()
        self.name = name
        self.age = age
        self.grade = grade
        self.regNo = regNo
        self.deleted: bool = False  # <-- soft delete flag


#this is a plain class to represent a student object
#it is just an object in memory...no database yet
# In-memory "database"