from pydantic import BaseModel

class users_model(BaseModel):
    firstname:str
    lastname:str
    username:str
    phonenumber:str