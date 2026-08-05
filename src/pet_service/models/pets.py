from typing import List

from pydantic import BaseModel

from pet_service.dto.pet_dto import Species, Status


class PetModel(BaseModel):
    id: int
    name: str
    image: str
    species: Species
    description: str
    status: Status = Status.available

    model_config = {"from_attributes": True}

class AllPetsResponse(BaseModel):
    pets: List[PetModel]

class CreatePetRequest(BaseModel):
    name: str
    image: str
    species: Species
    description: str

