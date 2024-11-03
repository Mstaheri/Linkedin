from fastapi import HTTPException , status

class SuccessFully(HTTPException):
    def __init__(self, id:str , operation:str):
        self.status_code = status.HTTP_200_OK
        self.detail = f"{operation} is {id} Successfully"

class SuccessFullyCreating(HTTPException):
    def __init__(self, id:str):
        self.status_code = status.HTTP_201_CREATED
        self.detail = f"created is {id} Successfully"

class IsNullException(HTTPException):
    def __init__(self, field: str):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = f"The {field} cannot be empty"

class NotNegativeException(HTTPException):
    def __init__(self, field: str):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = f"The {field} must not be negative"

class UsernamePasswordIncorrect(HTTPException):
    def __init__(self,):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.detail = "username or password is incorrect"

class TokenExpiredException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.detail = "Access denied: Your authentication token has expired"
        headers = {"WWW-Authenticate": "Bearer"}

class TokenMissingException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.detail = "Access denied: No authentication token provided"
        headers = {"WWW-Authenticate": "Bearer"}

class InvalidTokenException(HTTPException):
    def __init__(self):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.detail = "Access denied: The provided token is invalid"
        headers = {"WWW-Authenticate": "Bearer"}

class NotFoundException(HTTPException):
    def __init__(self, item: str):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = f"The desired {item} was not found"

class DuplicateException(HTTPException):
    def __init__(self, field: str):
        self.status_code = status.HTTP_409_CONFLICT
        self.detail = f"The {field} is duplicate"

class IncorrectFormatException(HTTPException):
    def __init__(self, field: str):
        self.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        self.detail = f"This format is not correct for {field}"

class ErrorCreating(HTTPException):
    def __init__(self, entity:str , e:str):
        self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        self.detail = f"Error creating {entity}:{e}"

class ErrorUpdate(HTTPException):
    def __init__(self, entity:str , e:str):
        self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        self.detail = f"Error update {entity}:{e}"

class ErrorDelete(HTTPException):
    def __init__(self, entity:str , e:str):
        self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        self.detail = f"Error delete {entity}:{e}"

class ErrorGet(HTTPException):
    def __init__(self, entity:str , e:str):
        self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        self.detail = f"Error get {entity}:{e}"



