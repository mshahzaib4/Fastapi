from fastapi import FastAPI, Depends # ingonre type
from typing import List, Optional

app = FastAPI()

class Usersignup(BaseModel):
    username: str = Field(..., title="Username", max_length=20, description="Username of the user", examples=["Shahaib yaqoob"])
    password: str = Field(..., title="Password", min_length=8, description="Password of the user", examples=["password123"])
    email: str

class settings (BaseModel):
    app_name:str = 'Chai App'
    admin_email:str = 'shahzaibmalik@gamil.com'

def get_settings():
    return settings()    

@app.post("/signup")
async def signup(user:Usersignup):
    return {
        "message": "User signed up successfully!",
        "user_data": user
    }
@app.get("/settings")
async def get_settings(setting: settings = Depends(get_settings)):
    return {
        "app_name": setting.app_name,
        "admin_email": setting.admin_email
    }
