from typing import Any

from adoption_agency_common import BOARouter
from adoption_agency_common import logger
from pet_service.messages.pet_messages import GetPets
from pet_service.models.pets import AllPetsResponse

pet_router = BOARouter()

@pet_router.get("/")
async def get_pets() -> AllPetsResponse:
    logger.debug("Fetching all pets")
    msg = GetPets(payload={})
    msg.payload["test"] = "test"
    res = await pet_router.send_message(message=msg, res_model=AllPetsResponse)
    # r = await res
    return res

@pet_router.post("/pets")
def get_2_pets(body: ) -> Any:
    logger.debug("Fetching all pets")
    return ["1","2"]