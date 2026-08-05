from typing import Any, List, Literal

from adoption_agency_common import BOARouter
from adoption_agency_common.fastapi_helpers.models.boa_models import BoaResponseModel
from adoption_agency_common.util import logger
from pet_service.dto.pet_dto import Status
from pet_service.messages.pet_messages import GetPets, CreatePet, GetPetById, GetAllPetsResponse, GenericPetResponse, \
    UpdatePetStatusById, DeletePetById, DeletePetResponse
from pet_service.models.pets import CreatePetRequest, PetModel

pet_router = BOARouter()

@pet_router.get("/")
async def get_available_pets() -> BoaResponseModel[List[PetModel]]:
    logger.debug("Fetching all pets")
    msg = GetPets()
    res = await pet_router.send_message(message=msg, res_model=GetAllPetsResponse)
    return BoaResponseModel(response=res.pets)

@pet_router.get("/{pet_id}")
async def get_pet_by_id(pet_id: int) -> BoaResponseModel[PetModel]:
    msg = GetPetById(id=pet_id)
    res = await pet_router.send_message(message=msg, res_model=GenericPetResponse)
    return BoaResponseModel[PetModel](response=res.pet)

@pet_router.put("/{pet_id}/{status}")
async def update_pet_status_by_id(pet_id: int, status: Literal[Status.adopted, Status.reserved]) -> BoaResponseModel[PetModel]:
    msg = UpdatePetStatusById(id=pet_id, status=status)
    res = await pet_router.send_message(message=msg, res_model=GenericPetResponse)
    return BoaResponseModel[PetModel](response=res.pet)

@pet_router.post("/addPet")
async def add_pet(body: CreatePetRequest) -> BoaResponseModel[PetModel]:
    msg = CreatePet(name=body.name, image=body.image, species=body.species, description=body.description)
    res = await pet_router.send_message(message=msg, res_model=GenericPetResponse)
    return BoaResponseModel[PetModel](response=res.pet)

@pet_router.delete("/removePet/{pet_id}")
async def remove_pet(pet_id: int) -> BoaResponseModel[DeletePetResponse]:
    msg = DeletePetById(id=pet_id)
    res = await pet_router.send_message(message=msg, res_model=DeletePetResponse)
    return BoaResponseModel[DeletePetResponse](response=res)