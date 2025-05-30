from pydantic import BaseModel
class UserProfile(BaseModel):
    name:str
    age:int
data='{"name":"BlackWidow", "age":"40"}'
user=UserProfile.model_validate_json(data)
print(user)