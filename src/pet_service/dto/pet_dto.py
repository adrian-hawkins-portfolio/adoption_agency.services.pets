from adoption_agency_common import BaseModel

from enum import Enum

from sqlalchemy import Enum as SQLEnum, String
from sqlalchemy.orm import Mapped, mapped_column

class Status(str, Enum):
    available = "available"
    reserved = "reserved"
    adopted = "adopted"

class Species(str, Enum):
    cat = "cat"
    dog = "dog"

class Pet(BaseModel):
    __tablename__ = "pet"
    __table_args__ = {"schema": "pet"}

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    image: Mapped[str] = mapped_column(String, nullable=False)
    species: Mapped[Species] = mapped_column(
        SQLEnum(Species, name="species"),
        nullable=False
    )
    description: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[Status] = mapped_column(
        SQLEnum(Status, name="status"),
        nullable=False,
        default=Status.available,
    )

