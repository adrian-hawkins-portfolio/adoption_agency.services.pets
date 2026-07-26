from typing import Any

from adoption_agency_common import BOARouter
from adoption_agency_common import logger

pet_router = BOARouter()

@pet_router.get("/")
def get_pets() -> Any:
    logger.debug("Fetching all pets")
    return ["1","2"]