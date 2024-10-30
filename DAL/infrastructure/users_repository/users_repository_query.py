from sqlalchemy.ext.asyncio import AsyncSession
from BLL.irepository.users_irepository.users_irepository_query import users_irepository_query
from DAL.persistence.models.user import User
import sqlalchemy as sa
from BLL.utils.secrets import pwd_context
from BLL.exceptions import username_password_incorrect


class users_repository_query(users_irepository_query):
    def __init__(self , db_session : AsyncSession):
        self.db_session = db_session
    
    async def get_all_async(self):
        query = sa.select(User)
        async with self.db_session as session:
            result = await session.scalars(query)
            users = result.all()
        return users

    async def get_bycode_async(self , username:str)->User:
        query = sa.select(User).where(User.username == username)
        async with self.db_session as session:
            result = await session.scalar(query)
        return result
    
    async def login(self ,username:str , password:str)->User:
        result = await (users_repository_query(self.db_session)
                        .get_bycode_async(username))
        if result is None:
            raise username_password_incorrect()
        if not pwd_context.verify(password , result.password):
            raise username_password_incorrect()
        return result
        


            