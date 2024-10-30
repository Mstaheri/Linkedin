from fastapi import HTTPException
from typing import Callable , TypeVar , Generic

T = TypeVar('T')
class operation_result(Generic[T]):
    def __init__(self , is_success:bool , exception:HTTPException , data = None):
        self.is_success = is_success
        self.exception = exception
        self.data = data
    
    @staticmethod
    def create_validator(param : T):
        return operation_result_extention(param)
        
class operation_result_extention:
    def __init__(self , param : T , exception:HTTPException = None ,is_success:bool = True):
        self.param = param
        self.exception = exception
        self.is_success = is_success
    
    def validate(self ,func:Callable[[T], bool], exception:HTTPException):
        predicate_result = func(self.param)
        if predicate_result:
            raise exception
        return operation_result_extention(self.param , None ,True)

    
    
    
    
    
