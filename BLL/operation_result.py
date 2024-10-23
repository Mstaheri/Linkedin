from fastapi import HTTPException
class operation_result:
    def __init__(self , is_success:bool , exception:HTTPException , data = None):
        self.is_success = is_success
        self.exception = exception
        self.data = data