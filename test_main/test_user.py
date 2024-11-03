import pytest
from unittest.mock import AsyncMock, patch
from httpx import AsyncClient
from main import app
from website.schema.operation_result_dto import OperationResult
from website.routers.users.users_command import UsersServicesCommand


@pytest.mark.asyncio
async def test_create_user_success():

    data = {
        "firstname": "mamad",
        "lastname": "salman",
        "username": "",
        "password": "5580",
        "email": "mstaheri1i1111.011@gmail.com",
        "phonenumber": "09306994906"
    }

    operation_result = OperationResult(
        is_success=True,
        exception={"detail": "created is aliaaaaa Successfully", "status_code": 201},
        data=None
    )
    with patch.object(UsersServicesCommand, "create_async", AsyncMock(return_value=operation_result)):
        
        async with AsyncClient(app=app, base_url="http://test") as client:
            response = await client.post("/users/create", json=data)
            
            assert response.status_code == 200
            json_response = response.json()
            assert json_response['is_success'] is True
            assert json_response['exception'] is not None
            assert json_response['data'] is None
            assert json_response['exception']['detail'] == "created is aliaaaaa Successfully"
            assert json_response['exception']['status_code'] == 201
