from sqlalchemy.ext.asyncio import AsyncSession
from BLL.domain.irepository.users_irepository.users_irepository_query import users_irepository_query
from DAL.persistence.models.user import User
import sqlalchemy as sa

class users_repository_query(users_irepository_query):
    def __init__(self , db_session : AsyncSession):
        self.db_session = db_session
    
    async def get_all_async(self):
        query = sa.select(User)
        async with self.db_session as session:
            result = await session.scalars(query)
        return result

    async def get_bycode_async(self , username:str):
        query = sa.select(User).where(User.username == username)
        async with self.db_session as session:
            result = await session.scalar(query)
        return result
            