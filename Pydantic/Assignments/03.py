from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
from typing import List, Optional, Dict


app = FastAPI()

student_db : Dict [int, dict] = {}
class Student(BaseModel):
    name: str = Field(..., min_length=2)
    age: int = Field(..., gt=16)
    email: str
    student_class: str 
    
class student_out(Student):
    id:int

@app.get("/")
def create_student():
    return {"Welcome to theStudent API"}

@app.post("/student", response_model=student_out)
def add_student(student_id:int, student: Student):
    if student_id in student_db:
        raise HttpException(status_code=400, detail="Student ID already exists")
    student_db[student_id] = student
    return {"id":student_id, **student.dict()}

# Get Student buy ID
@app.get("/student/{student_id}", response_model = student_out)
def get_student(student_id:int):
    if student_id in student_db:
        return student_db[student_id] 
    else:
        raise HttpException(status_code=404, detail="Student not found")

# Update Student
@app.put("/student/{student_id}", response_model = student_out)
def get_student(student_id:int, student:Student):
    if student_id in student_db:
        student_db[student_id] = student
    else:
        return {"message": f"Student with ID {student_id} deleted."}
       
# Delete Student

@app.delete("/student/{student_id}")
def delete_student(student_id:int):
    if student_id in student_db:
        del student_db[student_id]
        return {"message": f"Student with ID {student_id} deleted."}
    else:
        raise HttpException(status_code=404, detail="Student not found")