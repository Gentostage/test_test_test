from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.models import Patient


async def get_list_patients_diagnoses(api_db: AsyncSession, limit: int = 3) -> List[Patient]:
    query_patient = (
        select(Patient.id)
        .limit(limit)
    )
    patients_ids = (await api_db.execute(query_patient)).unique().scalars().all()
    ids = [patient for patient in patients_ids]

    query_patient = (
        select(Patient)
        .options(
            joinedload(Patient.diagnoses),
        )
        .where(Patient.id.in_(ids))
    )
    return (await api_db.execute(query_patient)).unique().scalars().all()