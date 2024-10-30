from dotenv import load_dotenv
import os
import jwt
from fastapi import Depends
from datetime import datetime, timedelta
from typing import Annotated
from BLL.exceptions import token_missing_exception , token_expired_exception,invalid_token_exception
from fastapi.security import OAuth2PasswordBearer
from DAL.persistence.engine import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from DAL.infrastructure.users_repository.users_repository_query import users_repository_query



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")
load_dotenv()
def generate(username: str):
    secret_key = os.getenv("SECRET_KEY")
    algorithm = os.getenv("ALGORITHM")
    expire_time = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
    expires_delta = datetime.utcnow() + timedelta(hours=int(expire_time))
        
        
    payload = {
        'username': username,
        'exp': expires_delta
    }

    token = jwt.encode(payload, secret_key, algorithm)
    return token
    
async def verify_token(jwt_token: Annotated[str, Depends(oauth2_scheme)] ,
                    db_session :Annotated[AsyncSession, Depends(get_db)]) -> dict:
    if jwt_token is None:
        raise token_missing_exception
    try:
        secret_key = os.getenv("SECRET_KEY")
        algorithm = os.getenv("ALGORITHM")
        token_data = jwt.decode(
              jwt_token, secret_key, algorithms=[algorithm]
        )
        if datetime.fromtimestamp(token_data["exp"]) < datetime.now():
            raise token_expired_exception
    except jwt.exceptions.PyJWTError:
        raise invalid_token_exception
        
    user = await (users_repository_query(db_session)
                  .get_bycode_async(token_data["username"]))
    if user is None:
        raise invalid_token_exception
    return user