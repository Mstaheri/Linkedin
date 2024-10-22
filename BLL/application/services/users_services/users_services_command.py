from BLL.domain.irepository.users_irepository.users_irepository_command import users_irepository_command
from DAL.persistence.models.user import User
from BLL.operation_result import operation_result
from BLL.const_messages import messages

class users_services_command:
    def __init__(self , users :users_irepository_command):
        self.users = users

    async def create_async(self,
                           firstname:str , 
                           lastname:str , 
                           username:str,
                           phonenumbar:str,
                           ):
        try:
            user = User(firstname = firstname ,
                     lastname = lastname,
                     username = username,
                       phonenumber = phonenumbar)
            await self.users.create_async(user)
            return operation_result(True ,
                                     messages.successfully.format(user.username ,
                                                                  "create"))
        
        except Exception as e:
            return operation_result(False ,messages.Errorـcreating("users",str(e)))
        
    async def update_async(self,
                           firstname:str , 
                           lastname:str , 
                           username:str,
                           phonenumbar:str,
                           ):
        try:
            user = User(firstname = firstname ,
                     lastname = lastname,
                     username = username,
                       phonenumber = phonenumbar)
            await self.users.update_async(user)
            return operation_result(True ,
                                     messages.successfully.format(user.username ,
                                                                  "update"))
        
        except Exception as e:
            return operation_result(False ,messages.Errorـupdate("users",str(e)))
        
    async def delete_async(self,username:str
                           ):
        try:
            await self.users.delete_async(username)
            return operation_result(True ,
                                     messages.successfully.format(username ,
                                                                  "delete"))
        
        except Exception as e:
            return operation_result(False ,messages.Error_delete("users",str(e)))
        

        
        