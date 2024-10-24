from fastapi import HTTPException , status

class successfully(HTTPException):
    def __init__(self, id:str , operation:str):
        self.status_code = status.HTTP_200_OK
        self.detail = f"{operation} is {id} Successfully"

class successfullyـcreating(HTTPException):
    def __init__(self, id:str):
        self.status_code = status.HTTP_201_CREATED
        self.detail = f"created is {id} Successfully"

class is_null_exception(HTTPException):
    def __init__(self, field: str):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = f"The {field} cannot be empty"

class not_negative_exception(HTTPException):
    def __init__(self, field: str):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = f"The {field} must not be negative"

class maximum_length_exception(HTTPException):
    def __init__(self, field: str, max_length: int):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = f"{field} cannot be more than {max_length} characters"

class not_found_exception(HTTPException):
    def __init__(self, item: str):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = f"The desired {item} was not found"

class duplicate_exception(HTTPException):
    def __init__(self, field: str):
        self.status_code = status.HTTP_409_CONFLICT
        self.detail = f"The {field} is duplicate"

class incorrect_format_exception(HTTPException):
    def __init__(self, field: str):
        self.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        self.detail = f"This format is not correct for {field}"

class Errorـcreating(HTTPException):
    def __init__(self, entity:str , e:str):
        self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        self.detail = f"Error creating {entity}:{e}"

class Error_update(HTTPException):
    def __init__(self, entity:str , e:str):
        self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        self.detail = f"Error update {entity}:{e}"

class Error_delete(HTTPException):
    def __init__(self, entity:str , e:str):
        self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        self.detail = f"Error delete {entity}:{e}"

class Error_get(HTTPException):
    def __init__(self, entity:str , e:str):
        self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        self.detail = f"Error get {entity}:{e}"