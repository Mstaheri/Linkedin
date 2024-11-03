from fastapi import APIRouter , Depends
from BLL.services.users_services.users_services_query import UsersServicesQuery
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from website.schema.operation_result_dto import OperationResult
from DAL.persistence.models.user import User



router = APIRouter(prefix="/users", tags=["users"])



@router.get('/get/{username}' , response_model=OperationResult[User])
async def GetByCode(username:str,
                    users_services:UsersServicesQuery = Depends(UsersServicesQuery)):
    user = await users_services.get_bycode_async(username)
    if  not user.is_success:
        raise user.exception
    return user


@router.get('/getAll' , response_model=OperationResult[list[User]])
async def GetAll(users_services:UsersServicesQuery = Depends(UsersServicesQuery)):
    user = await users_services.get_all_async()
    if  not user.is_success:
        raise user.exception
    return user

@router.post('/token')
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                users_services:UsersServicesQuery = Depends(UsersServicesQuery)):
    user = await users_services.login(form_data.username , form_data.password )
    if  not user.is_success:
        raise user.exception
    return {
        "access_token": user.data,
        "token_type": "bearer",
    }