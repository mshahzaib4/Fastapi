from fastapi import FastAPI

app = FastAPI()

@app.get("/")

async def read_root():
    return {"My Name is Shahzaib Yaqoob"}

@app.get("/age")
async def post_request():
    return {"Enter your age"}

#Define a path operation for the root path ("/")
@app.get("/age/{age}")
async def get_age(age:str):
    if age.isdigit():
        return {"My age is": age}
    else:
        return {"error": "Please enter a valid age"}

@app.get("/")
async def put_request():
    return {"This is a put request id"}