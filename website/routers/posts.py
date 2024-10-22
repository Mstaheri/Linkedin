from fastapi import APIRouter , Body
from website.schema.user_dto import users_model

router = APIRouter(prefix="/posts")


@router.post('/create')
async def Create(model : users_model = Body()):
    ...


@router.put('/update')
async def Update(model : users_model = Body()):
    ...


@router.get('/Code/{code}')
async def GetByCode(code):
    ...


@router.get('/getAll')
async def GetAll():
    ...
