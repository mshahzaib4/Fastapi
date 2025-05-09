from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
def root():
    return {  "message": "Welcome to the FastAPI Assignment" }
@app.get("/name")
def name():
    return {  "My Name is": "M Shahzaib Yaqoob" }
@app.get("/age/{age}")
def get_age(age:str):
    if age.isdigit():
        return {"Your Age is ": age}
    else:
        {  "error": "Please enter a valid age" }

@app.get("/validate-age/")
async def validate_age(age: int = Query(..., ge=10, le=100)):
    return {"Validated Age": age}