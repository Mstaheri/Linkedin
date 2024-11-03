from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa
from DAL.persistence.models.user import User
from DAL.infrastructure.users_repository.users_repository_query import UsersRepositoryQuery
from BLL.exceptions import DuplicateException , NotFoundException
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from DAL.persistence.engine import get_db
from fastapi import Depends
class UsersRepositoryCommand():
    def __init__(self , db_session :Annotated[AsyncSession, Depends(get_db)]):
        self.db_session = db_session
    
    async def create_async(self , user:User):
        result = (await UsersRepositoryQuery(self.db_session)
                  .get_bycode_async(user.username))
        if not result is None:
            raise DuplicateException(user.username)
        async with self.db_session as session:
            session.add(user)
            await session.commit()

    async def update_async(self , user:User):
        query = (sa.update(User)
         .where(User.username == user.username)
         .values(firstname=user.firstname,
                 lastname=user.lastname,
                 password=user.password,
                 email=user.email,
                 phonenumber = user.phonenumber))
        async with self.db_session as session:
            await session.execute(query)
            await session.commit()
    
    async def update_image_async(self , username:str , image_location:str):
        query = (sa.update(User)
         .where(User.username == username)
         .values(image=image_location))
        async with self.db_session as session:
            await session.execute(query)
            await session.commit()

    async def delete_async(self , username:str):
        result = (await UsersRepositoryQuery(self.db_session)
                  .get_bycode_async(username))
        if result is None:
            raise NotFoundException(username)
        async with self.db_session as session:
            await session.delete(result)
            await session.commit()
            
            
        
        
        
            
        
                
            
        

        
