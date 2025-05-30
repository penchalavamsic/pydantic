from typing import Optional
from pydantic import BaseModel
class User(BaseModel):
    name:str
    age:Optional[int]=None
user=User(name="Falcon")
print(user)