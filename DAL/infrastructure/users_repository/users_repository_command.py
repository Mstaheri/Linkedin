from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa
from DAL.persistence.models.user import User
from BLL.irepository.users_irepository.users_irepository_command import users_irepository_command
from DAL.infrastructure.users_repository.users_repository_query import users_repository_query
from BLL.exceptions import duplicate_exception , not_found_exception
class users_repository_command(users_irepository_command):
    def __init__(self , db_session : AsyncSession):
        self.db_session = db_session
    
    async def create_async(self , user:User):
        result = (await users_repository_query(self.db_session)
                  .get_bycode_async(user.username))
        if not result is None:
            raise duplicate_exception(user.username)
        async with self.db_session as session:
            session.add(user)
            await session.commit()

    async def update_async(self , user:User):
        query = (sa.update(User)
         .where(User.username == user.username)
         .values(firstname=user.firstname,
                 lastname=user.lastname,
                 password=user.password,
                 phonenumber = user.phonenumber))
        async with self.db_session as session:
            await session.execute(query)
            await session.commit()

    async def delete_async(self , username:str):
        result = (await users_repository_query(self.db_session)
                  .get_bycode_async(username))
        if result is None:
            raise not_found_exception(username)
        async with self.db_session as session:
            await session.delete(result)
            await session.commit()
            
            
        
        
        
            
        
                
            
        

        
