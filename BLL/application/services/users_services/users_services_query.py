from BLL.domain.irepository.users_irepository.users_irepository_query import users_irepository_query
from BLL.operation_result import operation_result
from BLL.exceptions import Error_get

class users_services_query:
    def __init__(self , users :users_irepository_query):
        self.users = users

    async def get_all_async(self):
        try:
            result = await self.users.get_all_async()
            return operation_result(True ,None,result)
        
        except Exception as e:
            return (operation_result
                    (False 
                     ,Error_get
                     (users_services_query.__name__,str(e))))
        
    async def get_bycode_async(self,username:str):
        try:
            result = await self.users.get_bycode_async(username)
            return operation_result(True ,None,result)
        
        except Exception as e:
            return (operation_result
                    (False 
                     ,Error_get
                     (users_services_query.__name__,str(e))))