from pydantic import BaseModel

class product( BaseModel ):
    id:int
    name:str
    price:float
    in_stock:bool

input_data  = {
    "id": 1,
    "name": "drink",
    "price": 70,
    "in_stock": True
    }    

user = product(**input_data)

print(user)

