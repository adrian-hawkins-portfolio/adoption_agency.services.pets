from adoption_agency_common.saga_manager.base_saga import SagaBase
from adoption_agency_common.saga_manager.decorators import saga, handle
from pet_service.messages.pet_messages import PetHttpResponse
from adoption_agency_common.util import logger

@saga
class PetHttpSaga(SagaBase):


    @handle(PetHttpResponse)
    async def pet_http_response(self, msg: PetHttpResponse) -> None:
        await self.send_response(msg)