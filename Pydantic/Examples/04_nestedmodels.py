from pydantic import BaseModel
from typing import List, Optional

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name:str
    address: Address

class Comment(BaseModel):
    id: int
    content: User
    reply: Optional[list["Comment"]] = None
Comment.model_rebuild()

adreess = Address(street="123 Main St", city="New York", zip_code="10001")
user = User(id=1, name="John Doe", address=adreess)
comment = Comment(id=1, content=user, reply=[Comment(id=2, content=user)])
print(adreess)
print(user)
print(comment) 
