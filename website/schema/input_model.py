from pydantic import BaseModel

class users_model(BaseModel):
    firstname:str
    lastname:str
    phonenumber:str