from pydantic import BaseModel, Field
from typing import Optional, List, Dict

class Employee(BaseModel):
    id:int
    name:str = Field(..., title="Employee Name", max_length=20, description="Name of the employee", examples=["Shahaib yaqoob"])
    age:int = Field(..., gt=18, le=65, description="Age of the employee", examples=[22])
    salary:float = Field(..., gt=0, description="Salary of the employee", examples=[50000])
    department:str = Field(..., title="Department", description="Department of the employee", examples=["IT","BSCS", "AI", "ML"])
    address:Optional[str] = Field("General", title="Address", description="Address of the employee", examples=["123 Main St"])
    skills:List[str] = Field(..., title="Skills", description="Skills of the employee", examples=[["Python", "FastAPI"]])
