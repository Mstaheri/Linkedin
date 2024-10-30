from abc import ABC, abstractmethod
from DAL.persistence.models.user import User
class users_irepository_query(ABC):
    
    @abstractmethod
    async def get_all_async(self):
        pass
    @abstractmethod
    async def get_bycode_async(self , username:str)->User:
        pass
    @abstractmethod
    async def login(self ,username:str , password:str)->User:
        pass