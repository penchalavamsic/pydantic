from pydantic import BaseModel
class Userprofile(BaseModel):
    name:str
    age:int
    email:str
user=Userprofile(name="RDJ",age="45",email="rdj45@gmail.com")
print(user)
print(user.name)