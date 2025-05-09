from pydantic import BaseModel, Field
from typing import List
from datetime import datetime 


class Product(BaseModel): 
    id: int
    name: str
    price: float

class Order(BaseModel):
    id: int
    products: list[Product]
    total_price: float = Field(..., gt=0)
    order_date: datetime = Field(default_factory=datetime.now)

# create user instence
order = Order(
    id=1,
    products=[
        Product(id=1, name="Laptop", price=1200.00),
        Product(id=2, name="Mouse", price=25.00)
    ],
    total_price=1225.00,
    order_date=datetime.now()
)
 # use Model to dump data to dict
order_dict = order.model_dump()
print(order_dict)
print("##############################################")
# use Model to dump data to json
order_json = order.model_dump_json()
print(order_json)