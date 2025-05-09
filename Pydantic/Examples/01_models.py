from pydantic import BaseModel

class User(BaseModel):
    id:int
    name:str
    is_active:bool
    age:int

input_data = {
    "id": 1,
    "name": "Shahzaib Yaqoob",
    "is_active": True,
    "age": 22
}

user = User(**input_data)
print(user)
