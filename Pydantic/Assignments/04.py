from fastapi import FastAPI, Field, HTTPException
from pydantic import BaseModel, EmailStr, constr
from typing import Dict, Optional


student_db: Dict[int, dict] = {}

class Student(BaseModel):
    name:str
    roll_number:int
    marks:dict[str,int]

class StudentResult(BaseModel):
    name: str
    roll_number: int
    total: int
    percentage: float
    grade: str

app = FastAPI()

@app.get("/")
async def Welcome():
    return {"message": "Welcome to the Student Result API"}

#add Student result
@app.post("/results/" response_model = StudentResult)
async def addresult(student:Student):
    if student.roll_number in student_db:
        raise HTTPException(status_code=400, detail="Roll number already exists")
    
    total = sum(student.marks.vales())
    percentage = total/(len(student.marks)*100) *100
    # Grade logic
    if percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    result = {
        "name": student.name,
        "roll_number": student.roll_number,
        "total": total,
        "percentage": round(percentage, 2),
        "grade": grade
    }
    student_db[student.roll_number] = result
    return result
@app.get("/results/{roll_number}", response_model=StudentResult)
def get_result(roll_number: int):
    result = student_db.get(roll_number)
    if not result:
        raise HTTPException(status_code=404, detail="Student not found")
    return result




