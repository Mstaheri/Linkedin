from fastapi import APIRouter , Body , Depends
from website.schema.user_dto import users_model
from BLL.application.services.users_services.users_services_command import users_services_command
from DAL.infrastructure.users_repository.users_repository_command import users_repository_command
from DAL.infrastructure.users_repository.users_repository_query import users_repository_query
from BLL.application.services.users_services.users_services_query import users_services_query
from typing import Annotated
from DAL.persistence.engine import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from BLL.operation_result import operation_result
from BLL.exceptions import Error_delete,incorrect_format_exception


router = APIRouter(prefix="/users")


@router.post('/create')
async def Create(db_session :Annotated[AsyncSession, Depends(get_db)],
                 model : users_model = Body()
                 ):
    user = (await users_services_command
            (users_repository_command(db_session))
            .create_async(
                model.firstname,
                model.lastname,
                model.username,
                model.phonenumber
            ))
    raise user.exception

@router.put('/update')
async def Update(db_session :Annotated[AsyncSession, Depends(get_db)],
                 model : users_model = Body()):
    user = (await users_services_command
            (users_repository_command(db_session))
            .update_async(
                model.firstname,
                model.lastname,
                model.username,
                model.phonenumber
            ))
    raise user.exception

@router.delete('/delete/{username}')
async def delete(db_session :Annotated[AsyncSession, Depends(get_db)],
                 username:str):
    user = (await users_services_command
            (users_repository_command(db_session))
            .delete_async(username))
    raise user.exception


@router.get('/get/{username}')
async def GetByCode(db_session :Annotated[AsyncSession, Depends(get_db)],
                    username:str):
    user = (await users_services_query
            (users_repository_query(db_session))
            .get_bycode_async(username))
    if  not user.is_success:
        raise user.exception
    return user.data


@router.get('/getAll')
async def GetAll(db_session :Annotated[AsyncSession, Depends(get_db)]):
    user = (await users_services_query
            (users_repository_query(db_session))
            .get_all_async())
    if  not user.is_success:
        raise user.exception
    return user.data
