from fastapi import HTTPException , status

class successfully(HTTPException):
    def __init__(self, entity:str , operation:str):
        self.status_code = status.HTTP_200_OK
        self.detail = f"{operation} is {entity} Successfully"

class successfullyـcreating(HTTPException):
    def __init__(self, entity:str):
        self.status_code = status.HTTP_201_CREATED
        self.detail = f"created is {entity} Successfully"



# class messages:
#     is_null = "The {0} cannot be empty"
#     incorrect_format = "This format is not correct for {0}"
#     incorrect_format_characters = "The format of the characters in the {0} is not correct"
#     duplicate = "The {0} is duplicate"
#     not_found = "The desired {0} was not found"
#     not_negative_or_zero = "The {0} must not be negative or zero"
#     not_negative = "The {0} must not be negative"
#     not_inventory = "The balance of {0} account in Bank {1} is {2}"
#     maximum_length = "{0} cannot be more than {1} characters"
#     not_between_number = "The {0} number must be between {1} and {2}"

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