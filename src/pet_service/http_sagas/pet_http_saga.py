from adoption_agency_common.saga_manager.base_saga import SagaBase
from adoption_agency_common.saga_manager.decorators import saga, handle
from pet_service.messages.pet_messages import GetAllPetsResponse, GenericPetResponse, DeletePetResponse

@saga
class PetHttpSaga(SagaBase):


    @handle(GetAllPetsResponse)
    async def pet_http_response(self, msg: GetAllPetsResponse) -> None:
        await self.send_response(msg)

    @handle(GenericPetResponse)
    async def pet_by_id_res(self, msg: GetAllPetsResponse) -> None:
        await self.send_response(msg)

    @handle(DeletePetResponse)
    async def delete_pet_res(self, msg: GetAllPetsResponse) -> None:
        await self.send_response(msg)