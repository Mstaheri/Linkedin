from BLL.operation_result import OperationResult
from BLL.exceptions import ErrorGet
from BLL.utils.jwt import generate
from DAL.infrastructure.users_repository.users_repository_query import UsersRepositoryQuery
from fastapi import Depends

class UsersServicesQuery:
    def __init__(self ,
                 users_repository :UsersRepositoryQuery = Depends(UsersRepositoryQuery)):
        self.users_repository = users_repository
    async def get_all_async(self):
        try:
            result = await self.users_repository.get_all_async()
            
            return OperationResult(True ,None,result)
        
        except Exception as e:
            return (OperationResult
                    (False ,ErrorGet
                     (UsersServicesQuery.__name__,str(e))))
        
    async def get_bycode_async(self,username:str):
        try:
            result = await self.users_repository.get_bycode_async(username)
            return OperationResult(True ,None,result)
        
        except Exception as e:
            return (OperationResult
                    (False ,ErrorGet
                     (UsersServicesQuery.__name__,str(e))))
        
    async def login(self,username:str , password:str):
        try:
            result = await self.users_repository.login(username , password)
            token = generate(result.username)
                
            return OperationResult(True ,None,token)
        
        except Exception as e:
            return (OperationResult
                    (False ,ErrorGet
                     (UsersServicesQuery.__name__,str(e))))