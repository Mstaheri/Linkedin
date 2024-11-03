from fastapi import APIRouter , Depends  , Body  , UploadFile , File
from website.schema.user_dto import users_model_input  , users_model_edit_input
from BLL.services.users_services.users_services_command import UsersServicesCommand
from typing import Annotated
from BLL.utils.jwt import verify_token
from website.schema.operation_result_dto import OperationResult


router = APIRouter(prefix="/users", tags=["users"])


@router.post('/create' , response_model= OperationResult)
async def Create(model : users_model_input = Body(), 
                 users_services:UsersServicesCommand = Depends(UsersServicesCommand)
                 ):
    result = await users_services.create_async(
                model.firstname,
                model.lastname,
                model.username,
                model.password,
                model.phonenumber,
                model.email,
            )
    if  not result.is_success:
        raise result.exception
    return result

@router.put('/update' , response_model=OperationResult)
async def Update(current_user: Annotated[users_model_input, Depends(verify_token)],
                 users_services:UsersServicesCommand = Depends(UsersServicesCommand),
                 model : users_model_edit_input = Body(),
                 ):
    result = await users_services.update_async(
                model.firstname,
                model.lastname,
                current_user.username,
                model.password,
                model.email,
                model.phonenumber,
            )
    if  not result.is_success:
        raise result.exception
    return result

@router.delete('/delete' , response_model=OperationResult)
async def delete(current_user: Annotated[users_model_input, Depends(verify_token)],
                 users_services:UsersServicesCommand = Depends(UsersServicesCommand)):
    result = await users_services.delete_async(current_user.username)
    if  not result.is_success:
        raise result.exception
    return result

@router.post("/image")
async def upload_image(current_user: Annotated[users_model_input, Depends(verify_token)],
                    users_services:UsersServicesCommand = Depends(UsersServicesCommand)
                    ,image:UploadFile = File(None)):
    result = await users_services.update_image_async(
                current_user.username,
                image
            )
    if  not result.is_success:
        raise result.exception
    return result
