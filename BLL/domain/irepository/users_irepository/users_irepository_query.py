from abc import ABC, abstractmethod

class users_irepository_query(ABC):
    
    @abstractmethod
    async def get_all_async(self):
        pass
    @abstractmethod
    async def get_bycode_async(self , username:str):
        pass