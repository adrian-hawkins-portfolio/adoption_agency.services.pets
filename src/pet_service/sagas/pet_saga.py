from sqlalchemy import select

from adoption_agency_common.database import session_local
from adoption_agency_common.saga_manager.base_saga import SagaBase
from adoption_agency_common.saga_manager.decorators import saga, handle
from pet_service.dto.pet_dto import Pet
from pet_service.messages.pet_messages import GetPets
from pet_service.messages.pet_messages import PetHttpResponse
from adoption_agency_common.util import logger
from pet_service.models.pets import AllPetsResponse, PetModel


@saga
class PetSaga(SagaBase):

    @handle(GetPets)
    async def get_all_pets(self, msg: GetPets) -> None:
        async with session_local() as session:
            result = await session.scalars(select(Pet))
            orm_pets = result.all()

            val = AllPetsResponse(
                pets=[PetModel.model_validate(pet) for pet in orm_pets]
            )
            resp_msg = PetHttpResponse(payload=val.model_dump(), existing_message=msg)
            logger.debug(f"Processing messsage with payload: {resp_msg.payload}")
            await self.send_message(resp_msg)
