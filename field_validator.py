from pydantic import BaseModel, field_validator
class UserProfile(BaseModel):
    name:str
    age:int =14
    email:str
    @field_validator('age')
    def Validate(cls, value):
        if value<18:
            raise ValueError("Age must be at leat 18")
        return value
user=UserProfile(name="Thor",age=17, email="thor14@gmail.com")
print(user)