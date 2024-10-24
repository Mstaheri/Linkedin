from BLL.domain.irepository.users_irepository.users_irepository_command import users_irepository_command
from DAL.persistence.models.user import User
from BLL.operation_result import operation_result
from BLL.exceptions import Errorـcreating , Error_delete,Error_update , successfully , successfullyـcreating

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
            return (operation_result
                    (True 
                     ,successfullyـcreating(user.username)))
        except Exception as e:
            return (operation_result
                    (False 
                     ,Errorـcreating
                     (users_services_command.__name__ ,str(e))))
        
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
            return (operation_result
                    (True ,
                     successfully
                     (user.username ,
                     users_services_command.update_async.__name__)))
        except Exception as e:
            return (operation_result
                    (False 
                     ,Error_update
                     (users_services_command.__name__,str(e))))
        
    async def delete_async(self,username:str):
        try:
            await self.users.delete_async(username)
            return (operation_result
                    (True ,
                     successfully
                     (username
                      ,users_services_command.delete_async.__name__)))
        
        except Exception as e:
            return (operation_result
                    (False ,
                     Error_delete
                     (users_services_command.__name__ , str(e))))
        

        
        