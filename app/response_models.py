from datetime import datetime
from typing import List

from pydantic import BaseModel
from pydantic.types import UUID4


class PatientResponseModel(BaseModel):
    id: UUID4
    date_of_birth: datetime
    diagnoses: List[str]
    created_at: datetime

    class Config:
        orm_mode = True


class TokenResponse(BaseModel):
    token: str
