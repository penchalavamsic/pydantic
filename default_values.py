from pydantic import BaseModel
class UserProfile(BaseModel):
    name:str
    age:int=45 #default value
    email:str
    is_active:bool=True #default value
user=UserProfile(name="CaptainAmerica",email="captain45@gamil.com")
print(user)