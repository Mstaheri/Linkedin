from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy as sa
from DAL.persistence.models.user import User
from BLL.domain.irepository.users_irepository.users_irepository_command import users_irepository_command
class users_repository_command(users_irepository_command):
    def __init__(self , db_session : AsyncSession):
        self.db_session = db_session
    
    async def create_async(self , user:User):
        async with self.db_session as session:
            session.add(user)
            await session.commit()

    async def update_async(self , user:User):
        query = (sa.update(User)
         .where(User.username == user.username)
         .values(firstname=user.firstname,
                 lastname= user.lastname,
                 phonenumber = user.phonenumber))
        async with self.db_session as session:
            await session.execute(query)
            await session.commit()

    async def delete_async(self , username:str):
        query = sa.delete(User).where(User.username == username)
        async with self.db_session as session:
            await session.execute(query)
            await session.commit()
            
            
        
        
        
            
        
                
            
        

        
