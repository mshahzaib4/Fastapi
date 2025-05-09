from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")

async def read_root():
    return {"Hello": "World" ," Hello": "John "}

