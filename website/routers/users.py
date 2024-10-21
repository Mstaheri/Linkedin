from fastapi import APIRouter , Body , Depends
from website.schema.input_model import users_model
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from DAL.users import users
from DAL.db.engine import get_db

router = APIRouter(prefix="/users")


@router.post('/create')
async def Create(db_session :Annotated[AsyncSession, Depends(get_db)] 
           ,model : users_model = Body()):
    user = await users(db_session).create_async(model.firstname,
                                    model.lastname,
                                    model.phonenumber)
    return user


@router.put('/update')
async def Update(model : users_model = Body()):
    ...


@router.get('/Code/{code}')
async def GetByCode(code):
    ...


@router.get('/getAll')
async def GetAll():
    ...
