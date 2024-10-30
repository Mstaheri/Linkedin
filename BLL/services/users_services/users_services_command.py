from BLL.irepository.users_irepository.users_irepository_command import users_irepository_command
from DAL.persistence.models.user import User
from BLL.operation_result import operation_result
from BLL.exceptions import Errorـcreating , Error_delete,Error_update , successfully , successfullyـcreating
from BLL.utils.secrets import pwd_context
from fastapi import UploadFile , BackgroundTasks
from BLL.utils.email import send_email
import os

class users_services_command:
    def __init__(self , users :users_irepository_command):
        self.users = users

    async def create_async(self,
                           firstname:str, 
                           lastname:str, 
                           username:str,
                           password:str,
                           phonenumbar:str,
                           email,
                           image:UploadFile,
                           backgroundTasks:BackgroundTasks
                           ):
        try:
            image_location = None
            if not image is None :
                image_location = os.path.join("/home/mst/Downloads/Linkedin/uploads",username)
            user_pwd = pwd_context.hash(password)
            user = User(firstname = firstname ,
                     lastname = lastname,
                     username = username,
                     password = user_pwd,
                       phonenumber = phonenumbar,
                       email = email,
                       image = image_location)
            await self.users.create_async(user)
            if not image_location is None :
                with open(image_location, "wb") as f:
                    f.write(await image.read())
            
            sender = os.getenv("sender_email")
            sender_password = os.getenv("sender_password")

            send_email (sender , sender_password
                                     , email , "سلام" , "ثبت نام شدید")

            return (operation_result
                    (True ,successfullyـcreating(user.username)))
        except Exception as e:
            return (operation_result
                    (False ,Errorـcreating
                     (users_services_command.__name__ ,str(e))))
        
    async def update_async(self,
                           firstname:str , 
                           lastname:str , 
                           username:str,
                           password:str,
                           phonenumbar:str,
                           image:UploadFile
                           ):
        try:
            image_location = None
            if not image is None:
                image_location = os.path.join("/home/mst/Downloads/Linkedin/uploads",username)
            user = User(firstname = firstname ,
                     lastname = lastname,
                     username = username,
                     password = password,
                       phonenumber = phonenumbar,
                       image=image)
            await self.users.update_async(user)
            if not image_location is None:
                if os.path.exists(image_location):
                    os.remove(image_location)
                with open(image_location, "wb") as f:
                    f.write(await image.read())
            return (operation_result
                    (True ,successfully
                     (user.username ,users_services_command.update_async.__name__)))
        except Exception as e:
            return (operation_result
                    (False ,Error_update
                     (users_services_command.__name__,str(e))))
        
    async def delete_async(self,username:str):
        try:
            await self.users.delete_async(username)
            return (operation_result
                    (True ,successfully
                     (username,users_services_command.delete_async.__name__)))
        
        except Exception as e:
            return (operation_result
                    (False ,Error_delete
                     (users_services_command.__name__ , str(e))))
        

        
        