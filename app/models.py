import uuid
from datetime import datetime
from typing import List

from app.db import Base
from sqlalchemy import Column, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy import (String, ForeignKey)


class UUIDMixin:
    """Добавляет к модели поле id"""
    __abstract__ = True
    id: uuid.UUID = Column(
        UUID(as_uuid=True),
        primary_key=True,
        nullable=False,
        default=uuid.uuid4,
        comment='Идентификатор'
    )


class CreatedMixin:
    """Добавляет к модели поля created_at."""

    __abstract__ = True

    created_at: Column = Column(DateTime(timezone=True), server_default=func.now())


class BaseModel(Base, UUIDMixin):
    __abstract__ = True


class Patient(BaseModel, CreatedMixin):
    __tablename__ = 'patients'

    date_of_birth: datetime = Column(DateTime(timezone=True), nullable=False, comment='Дата рождения')
    diagnoses: List['Diagnoses'] = relationship(
        'Diagnoses',
        cascade='all, delete-orphan',
    )


class Diagnoses(BaseModel):
    __tablename__ = 'diagnoses'

    patient_id: uuid.UUID = Column(
        UUID(as_uuid=True),
        ForeignKey('patients.id', ondelete='CASCADE'),
        nullable=False,
        comment='Идентификатор ',
    )
    status = Column(String, comment='Название диагноза')
