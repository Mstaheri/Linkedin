class operation_result:
    def __init__(self , is_success:bool , message:str , data = None):
        self.is_success = is_success
        self.message = message
        self.data = data

    def __str__(self):
        return f'{self.is_success}=>({self.message})'