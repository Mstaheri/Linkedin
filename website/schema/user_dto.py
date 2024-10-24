from pydantic import BaseModel , validator
from BLL.operation_result import operation_result
from BLL.exceptions import incorrect_format_exception , maximum_length_exception , is_null_exception

class users_model(BaseModel):
    firstname:str
    lastname:str
    username:str
    phonenumber:str

    @validator('firstname')
    def validate_firstname(cls , value : str):
        result : operation_result = (operation_result[str].create_validator(value)
        .validate(lambda x:x == "" or x == None ,is_null_exception('firstname'))
        .validate(lambda x:len(x) > 50 ,maximum_length_exception('firstname' , 50)))
        
        if not result.is_success:
            raise result.exception
        return value
    
    @validator('lastname')
    def validate_lastname(cls , value : str):
        result : operation_result = (operation_result[str].create_validator(value)
        .validate(lambda x:x == None ,is_null_exception('lastname'))
        .validate(lambda x:len(x) > 50 ,maximum_length_exception('lastname' , "50")))
        if not result.is_success:
            raise result.exception
        return value
    
    @validator('username')
    def validate_username(cls , value : str):
        result : operation_result = (operation_result[str].create_validator(value)
        .validate(lambda x:x == None ,is_null_exception('username'))
        .validate(lambda x:len(x) > 50 ,maximum_length_exception('username' , "50")))
        if not result.is_success:
            raise result.exception
        return value

    @validator('phonenumber')
    def validate_phonenumber(cls , value : str):
        result : operation_result = (operation_result[str].create_validator(value)
        .validate(lambda x:len(x) != 11 ,incorrect_format_exception('phonenumber'))
        .validate(lambda x:not str(x).isdigit() ,incorrect_format_exception('phonenumber'))
        .validate(lambda x:not str(x).startswith("09") ,incorrect_format_exception('phonenumber')))
        if not result.is_success:
            raise result.exception
        return value
    
    



