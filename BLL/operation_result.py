from fastapi import HTTPException
from typing import Callable , TypeVar , Generic

T = TypeVar('T')
class OperationResult(Generic[T]):
    def __init__(self , is_success:bool , exception:HTTPException , data = None):
        self.is_success = is_success
        self.exception = exception
        self.data = data
    
    @staticmethod
    def create_validator(param : T):
        return OperationResultExtention(param)
        
class OperationResultExtention:
    def __init__(self , param : T , exception:HTTPException = None ,is_success:bool = True):
        self.param = param
        self.exception = exception
        self.is_success = is_success
    
    def validate(self ,func:Callable[[T], bool], exception:HTTPException):
        predicate_result = func(self.param)
        if predicate_result:
            raise exception
        return OperationResultExtention(self.param , None ,True)

    
    
    
    
    
