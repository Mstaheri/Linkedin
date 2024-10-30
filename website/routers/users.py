from fastapi import APIRouter , Depends , Query  , UploadFile , File , BackgroundTasks
from website.schema.user_dto import users_model_input  , users_model_edit_input
from BLL.services.users_services.users_services_command import users_services_command
from DAL.infrastructure.users_repository.users_repository_command import users_repository_command
from DAL.infrastructure.users_repository.users_repository_query import users_repository_query
from BLL.services.users_services.users_services_query import users_services_query
from typing import Annotated
from DAL.persistence.engine import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm
from BLL.utils.jwt import verify_token


router = APIRouter(prefix="/users", tags=["users"])


@router.post('/create')
async def Create(db_session :Annotated[AsyncSession, Depends(get_db)],
                 background_tasks: BackgroundTasks,
                 model : users_model_input = Query() , 
                 image: Annotated[UploadFile, File(description="Upload a single file")] = None
                 ):
    user = (await users_services_command
            (users_repository_command(db_session))
            .create_async(
                model.firstname,
                model.lastname,
                model.username,
                model.password,
                model.phonenumber,
                model.email,
                image,
                background_tasks
            ))
    raise user.exception

@router.put('/update')
async def Update(db_session :Annotated[AsyncSession, Depends(get_db)],
                 current_user: Annotated[users_model_input, Depends(verify_token)],
                 model : users_model_edit_input = Query(),
                 image: Annotated[UploadFile, File(description="Upload a single file")] = None
                 ):
    user = (await users_services_command
            (users_repository_command(db_session))
            .update_async(
                model.firstname,
                model.lastname,
                current_user.username,
                model.password,
                model.phonenumber,
                image
            ))
    raise user.exception

@router.delete('/delete')
async def delete(db_session :Annotated[AsyncSession, Depends(get_db)],
                 current_user: Annotated[users_model_input, Depends(verify_token)]):
    user = (await users_services_command
            (users_repository_command(db_session))
            .delete_async(current_user.username))
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

@router.post('/token')
async def login(db_session :Annotated[AsyncSession, Depends(get_db)],
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = (await users_services_query
            (users_repository_query(db_session))
            .login(form_data.username , form_data.password ))
    if  not user.is_success:
        raise user.exception
    return {
        "access_token": user.data,
        "token_type": "bearer",
    }
