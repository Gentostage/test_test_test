from calendar import timegm
from datetime import datetime, timedelta

from jose import jwt
from pydantic import BaseModel
from pydantic.types import UUID4

from app.config import config


class TokenData(BaseModel):
    id: UUID4
    is_doctor: bool


class User(BaseModel):
    id: UUID4
    is_doctor: bool


def decode_token(token: str) -> User:
    token_data = jwt.decode(token, config.secret_key, algorithms=[config.algorithm])
    return User(**token_data)


def create_access_token(
    user: User,
    token_type: str = 'session',
) -> str:
    """Создание токена доступа."""

    to_encode = {}

    current = datetime.utcnow()
    expire = current + timedelta(days=1)
    timestamp = timegm(current.utctimetuple())
    to_encode.update(
        {
            'id': str(user.id),
            'is_doctor': user.is_doctor,
            'sub': token_type,
            'nbf': timestamp,
            'iat': timestamp,
            'exp': timegm(expire.utctimetuple()),
        }
    )

    encoded_jwt = jwt.encode(to_encode, config.secret_key, algorithm=config.algorithm)

    return encoded_jwt
