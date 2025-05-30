from pydantic import BaseModel
class Userprofile(BaseModel):
    name:str
    age:int
user=Userprofile(name="Hawkeye",age="45")
a=user.json()
print(a)