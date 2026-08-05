from typing import List

from adoption_agency_common.saga_manager.base_message import BaseMessage
from pet_service.dto.pet_dto import Status, Species
from pet_service.models.pets import PetModel


class GetPets(BaseMessage):
    pass

class GetPetById(BaseMessage):
    id: int

class UpdatePetStatusById(BaseMessage):
    id: int
    status: Status

class CreatePet(BaseMessage):
    name: str
    image: str
    species: Species
    description: str

class ReservePet(BaseMessage):
    id: str

class DeletePetById(BaseMessage):
    id: int


class GetAllPetsResponse(BaseMessage):
    pets: List[PetModel]

class GenericPetResponse(BaseMessage):
    pet: PetModel

class DeletePetResponse(BaseMessage):
    id: int
    success: bool
