from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def Wellcome():
    return {"Message": "Welcome to the Student Record System" }
# Define a Pydantic model for student data
class Student(BaseModel):
    name: str
    age: int
    student_class: str

# POST route to add a new student
@app.get("/students/")
async def add_student(student: Student):
    return {
        "message": "Student added successfully!",
        "student_data": student
    }