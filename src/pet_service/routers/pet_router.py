from typing import Any

from petstore_common import BOARouter
from petstore_common import logger

pet_router = BOARouter()

@pet_router.get("/")
def get_pets() -> Any:
    logger.debug("Fetching all pets")
    return ["1","2"]