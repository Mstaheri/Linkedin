from sqlalchemy.ext.asyncio import AsyncSession
from .db.models.user import User
class users:
    def __init__(self , db_session : AsyncSession) -> None:
        self.db_session = db_session
    
    async def create_async(self , firstname:str , lastname:str , phonenumbar:str) ->User:
        user = User(firstname= firstname ,
                     lastname = lastname,
                       phonenumber = phonenumbar)
        async with self.db_session as session:
            session.add(user)
        return user
