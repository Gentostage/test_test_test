import uuid
from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.auth import create_access_token, User
from app.db import get_db
from app.depends import get_current_user
from app.response_models import PatientResponseModel, TokenResponse
from app.services import get_patient

patients_router = APIRouter(prefix='/patients', tags=['Patient'])


@patients_router.get(
    "/",
    response_model=List[PatientResponseModel],
    responses={
        status.HTTP_200_OK: {'description': 'List patients'},
        status.HTTP_403_FORBIDDEN: {'description': 'access denied'}
    }
)
async def get_list_patients(
    user: User = Depends(get_current_user),
    api_db: AsyncSession = Depends(get_db),
) -> List[PatientResponseModel]:
    return await get_patient(api_db, user)


auth_router = APIRouter(prefix='/auth', tags=['Auth'])

@auth_router.get("/", response_model=TokenResponse)
async def get_token(
    is_doctor: bool = Query(False, description='Это доктор')
) -> TokenResponse:
    """Получаем токен авторизации"""
    user = User(id=uuid.uuid4(), is_doctor=is_doctor)
    return TokenResponse(token=create_access_token(user))
