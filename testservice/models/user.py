from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Boolean
from sqlalchemy.dialects.postgresql import JSONB, UUID
from uuid import uuid4
from testservice.models.base import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(UUID, primary_key=True, default=lambda: str(uuid4()), index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    location = Column(String, nullable=False)
