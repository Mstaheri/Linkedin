from pydantic import BaseModel , validator , Field , EmailStr
from BLL.operation_result import operation_result
from BLL.exceptions import incorrect_format_exception

class users_model_input(BaseModel):
    firstname: str = Field(..., min_length=1, max_length=50)
    lastname: str = Field(..., min_length=1, max_length=50)
    username: str = Field(..., min_length=1, max_length=50)
    password: str = Field(..., min_length=1, max_length=200)
    email: EmailStr
    phonenumber:str = Field(None)

    @validator('phonenumber')
    def validate_phonenumber(cls , value : str):
        if not value == "" or value == None:
            (operation_result[str].create_validator(value)
            .validate(lambda x:len(x) != 11 ,incorrect_format_exception('phonenumber'))
            .validate(lambda x:not str(x).isdigit() ,incorrect_format_exception('phonenumber'))
            .validate(lambda x:not str(x).startswith("09") ,incorrect_format_exception('phonenumber')))
            return value
        return value
    
class users_model_edit_input(BaseModel):
    firstname: str = Field(..., min_length=1, max_length=50)
    lastname: str = Field(..., min_length=1, max_length=50)
    password: str = Field(..., min_length=1, max_length=200)
    phonenumber:str = Field(None , max_length=11)

    @validator('phonenumber')
    def validate_phonenumber(cls , value : str):
        if not value == "" or value == None:
            (operation_result[str].create_validator(value)
            .validate(lambda x:len(x) != 11 ,incorrect_format_exception('phonenumber'))
            .validate(lambda x:not str(x).isdigit() ,incorrect_format_exception('phonenumber'))
            .validate(lambda x:not str(x).startswith("09") ,incorrect_format_exception('phonenumber')))
            return value
        return value
