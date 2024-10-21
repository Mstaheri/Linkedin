from pydantic import BaseModel

class users(BaseModel):
    firstname:str
    lastname:str
    phonenumber:str