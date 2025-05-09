from pydantic import BaseModel, Field, model_validator, computed_field, field_validator

class user(BaseModel):
    username: str
    @field_validator("username")
    def check_username(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters long")
        return v
    
    class SignupData(BaseModel):
        password: str
        confirm_password: str
        @model_validator(mode="after")
        def check_password(cls, values):
            if values.password != values.confirm_password:
                raise ValueError("Passwords do not match")
            return values

class product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool

    @computed_field
    def is_expensive(self) -> bool:
        return self.price > 100