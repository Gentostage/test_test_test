from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.auth import decode_token, User

bearer_scheme = HTTPBearer(bearerFormat='JWT')


async def get_current_user(
    http_auth: HTTPAuthorizationCredentials = Depends(bearer_scheme)
) -> User:
    user_data = decode_token(http_auth.credentials)
    return user_data
