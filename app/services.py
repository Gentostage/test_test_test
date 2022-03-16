from typing import List

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.auth import User
from app.cruds import get_list_patients_diagnoses
from app.response_models import PatientResponseModel


async def get_patient(api_db: AsyncSession, user: User) -> List[PatientResponseModel]:
    if not user.is_doctor:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Access denied',
        )
    patients = await get_list_patients_diagnoses(api_db)
    result = []
    for patient in patients:
        result.append(
            PatientResponseModel(
                id=patient.id,
                date_of_birth=patient.date_of_birth,
                diagnoses=[diag.status for diag in patient.diagnoses],
                created_at=patient.created_at
            )
        )

    return result
