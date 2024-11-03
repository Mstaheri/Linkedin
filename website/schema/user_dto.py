from pydantic import BaseModel , field_validator , Field , EmailStr
from BLL.operation_result import OperationResult
from BLL.exceptions import IncorrectFormatException


class users_model_input(BaseModel):
    firstname: str = Field(..., min_length=1, max_length=50)
    lastname: str = Field(..., min_length=1, max_length=50)
    username: str = Field(..., min_length=1, max_length=50)
    password: str = Field(..., min_length=1, max_length=200)
    email: EmailStr
    phonenumber:str = Field(None , max_length=11)
#rejex
    @field_validator('phonenumber')
    def validate_phonenumber(cls , value : str):
        if not value == "" or value == None:
            (OperationResult[str].create_validator(value)
            .validate(lambda x:len(x) != 11 ,IncorrectFormatException('phonenumber'))
            .validate(lambda x:not str(x).isdigit() ,IncorrectFormatException('phonenumber'))
            .validate(lambda x:not str(x).startswith("09") ,IncorrectFormatException('phonenumber')))
            return value
        return value
    
class users_model_edit_input(BaseModel):
    firstname: str = Field(..., min_length=1, max_length=50)
    lastname: str = Field(..., min_length=1, max_length=50)
    password: str = Field(..., min_length=1, max_length=200)
    email: EmailStr
    phonenumber:str = Field(None , max_length=11)
    

    @field_validator('phonenumber')
    def validate_phonenumber(cls , value : str):
        if not value == "" or value == None:
            (OperationResult[str].create_validator(value)
            .validate(lambda x:len(x) != 11 ,IncorrectFormatException('phonenumber'))
            .validate(lambda x:not str(x).isdigit() ,IncorrectFormatException('phonenumber'))
            .validate(lambda x:not str(x).startswith("09") ,IncorrectFormatException('phonenumber')))
            return value
        return value

