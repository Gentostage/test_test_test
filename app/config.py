from typing import Optional, Dict, Any

from pydantic import BaseSettings, PostgresDsn, validator


class AsyncPostgresDsn(PostgresDsn):
    allowed_schemes = {'postgresql+asyncpg'}


class Config(BaseSettings):
    # Секретный ключ для подписи токена JWT.
    secret_key: str = 'key'
    # Алгоритм хэширования подписи JWT.
    algorithm: str = 'HS256'

    # Подключение к базе
    db_server: str = 'localhost'
    db_port: str = '5432'
    db_user: str = 'postgres'
    db_password: str = 'postgres'
    db_name: str = 'postgres'
    db_dsn: Optional[AsyncPostgresDsn] = None

    @validator('db_dsn', pre=True)
    def assemble_db_connection(cls, db_dsn: Optional[str], values: Dict[str, Any]) -> str:
        if isinstance(db_dsn, str):
            return db_dsn
        return AsyncPostgresDsn.build(
            scheme='postgresql+asyncpg',
            user=values.get('db_user'),
            password=values.get('db_password'),
            host=values.get('db_server', 'db'),
            port=values.get('db_port'),
            path=f"/{values.get('db_name', '')}",
        )

    host: str = 'localhost'
    port: int = 8000


config = Config()
