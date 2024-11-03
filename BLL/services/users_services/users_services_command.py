from DAL.persistence.models.user import User
from BLL.operation_result import OperationResult
from BLL.exceptions import ErrorCreating , ErrorDelete,ErrorUpdate , SuccessFully , SuccessFullyCreating
from BLL.utils.secrets import pwd_context
from fastapi import UploadFile , BackgroundTasks , Depends
from DAL.infrastructure.users_repository.users_repository_command import UsersRepositoryCommand
from BLL.utils.email import send_email
import os

class UsersServicesCommand:
    def __init__(self ,
                 background_tasks: BackgroundTasks , 
                 users_repository :UsersRepositoryCommand = Depends(UsersRepositoryCommand)):
        self.users_repository = users_repository
        self.background_tasks = background_tasks
    async def create_async(self,
                           firstname:str, 
                           lastname:str, 
                           username:str,
                           password:str,
                           phonenumbar:str,
                           email
                           ):
        try:
            user_pwd = pwd_context.hash(password)
            user = User(firstname = firstname ,
                    lastname = lastname,
                    username = username,
                    password = user_pwd,
                    phonenumber = phonenumbar,
                    image=None,
                    email = email
                    )
            await self.users_repository.create_async(user)
            
            sender = os.getenv("sender_email")
            sender_password = os.getenv("sender_password")

            self.background_tasks.add_task(send_email ,sender , sender_password
                                     , email , "سلام" , "ثبت نام شدید")

            return (OperationResult
                    (True ,SuccessFullyCreating(user.username)))
        except Exception as e:
            return (OperationResult
                    (False ,ErrorCreating
                     (UsersServicesCommand.__name__ ,str(e))))
        
    async def update_async(self,
                           firstname:str , 
                           lastname:str , 
                           username:str,
                           password:str,
                           email,
                           phonenumbar:str,
                           ):
        try:
            user = User(firstname = firstname ,
                    lastname = lastname,
                    username = username,
                    password = password,
                    email=email,
                    phonenumber = phonenumbar,
                    image=None)
            await self.users.update_async(user)
            return (OperationResult
                    (True ,SuccessFully
                     (user.username ,UsersServicesCommand.update_async.__name__)))
        except Exception as e:
            return (OperationResult
                    (False ,ErrorUpdate
                     (UsersServicesCommand.__name__,str(e))))
        
    async def update_image_async(self,
                           username:str,
                           image:UploadFile
                           ):
        try:
            image_location = None
            if not image is None:
                image_location = os.path.join("/home/mst/Downloads/Linkedin/uploads",username)
            await self.users.update_image_async(username , image_location)
            if not image_location is None:
                if os.path.exists(image_location):
                    os.remove(image_location)
                with open(image_location, "wb") as f:
                    f.write(await image.read())
            return (OperationResult
                    (True ,SuccessFully
                     (username ,UsersServicesCommand.update_image_async.__name__)))
        except Exception as e:
            return (OperationResult
                    (False ,ErrorUpdate
                     (UsersServicesCommand.__name__,str(e))))
        
    async def delete_async(self,username:str):
        try:
            await self.users.delete_async(username)
            return (OperationResult
                    (True ,SuccessFully
                     (username,UsersServicesCommand.delete_async.__name__)))
        
        except Exception as e:
            return (OperationResult
                    (False ,ErrorDelete
                     (UsersServicesCommand.__name__ , str(e))))
        

        
        