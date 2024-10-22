from BLL.domain.irepository.users_irepository.users_irepository_query import users_irepository_query
from DAL.persistence.models.user import User
from BLL.operation_result import operation_result
from BLL.const_messages import messages

class users_services_query:
    def __init__(self , users :users_irepository_query):
        self.users = users

    async def get_all_async(self):
        try:
            result = await self.users.get_all_async()
            return operation_result(True ,
                                     messages.successfully.format("get_all",
                                                                  ""),
                                                                  result)
        
        except Exception as e:
            return operation_result(False ,messages.Error_get("users",str(e)))
        
    async def get_bycode_async(self,username:str):
        try:
            result = await self.users.get_bycode_async(username)
            return operation_result(True ,
                                     messages.successfully.format("get_bycode" ,
                                                                  ""),
                                                                  result)
        
        except Exception as e:
            return operation_result(False ,messages.Error_get("users",str(e)))