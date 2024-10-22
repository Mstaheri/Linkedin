from abc import ABC, abstractmethod
from DAL.persistence.models.user import User

class users_irepository_command(ABC):
    
    @abstractmethod
    async def create_async(self ,user : User):
        pass
    @abstractmethod
    async def update_async(self , user : User):
        pass
    @abstractmethod
    async def delete_async(self , username:str,):
        pass
    