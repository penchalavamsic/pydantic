from pydantic import BaseModel
class Address(BaseModel):
    addr:str
    zipcode:int
class Userprofile(BaseModel):
    name:str
    age:int
    email:str
    address:Address
a=Address(addr="Newyork",zipcode=1234567)
ad=Userprofile(name="Hulk",age=45,email="hulk45@gmail.com",address=a)
print(ad)