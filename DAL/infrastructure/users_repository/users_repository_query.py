from sqlalchemy.ext.asyncio import AsyncSession
from DAL.persistence.engine import get_db
from fastapi import Depends
from typing import Annotated
from DAL.persistence.models.user import User
import sqlalchemy as sa
from BLL.utils.secrets import pwd_context
from BLL.exceptions import UsernamePasswordIncorrect


class UsersRepositoryQuery():
    def __init__(self , db_session :Annotated[AsyncSession, Depends(get_db)]):
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
        result = await (UsersRepositoryQuery(self.db_session)
                        .get_bycode_async(username))
        if result is None:
            raise UsernamePasswordIncorrect()
        if not pwd_context.verify(password , result.password):
            raise UsernamePasswordIncorrect()
        return result
        


            