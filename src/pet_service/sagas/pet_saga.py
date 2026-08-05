# from sqlalchemy import select
from sqlalchemy import update, delete, select, insert

from adoption_agency_common.database import session_local
from adoption_agency_common.saga_manager.base_saga import SagaBase
from adoption_agency_common.saga_manager.decorators import saga, handle
from pet_service.dto.pet_dto import Pet, Status
from pet_service.messages.pet_messages import GetPets, CreatePet, GetPetById, GenericPetResponse, UpdatePetStatusById, \
    DeletePetById, DeletePetResponse
from pet_service.messages.pet_messages import GetAllPetsResponse
from adoption_agency_common.util import logger
from pet_service.models.pets import AllPetsResponse, PetModel, CreatePetRequest


@saga
class PetSaga(SagaBase):

    @handle(GetPets)
    async def get_all_pets(self, msg: GetPets) -> None:
        async with session_local() as session:
            result = await session.scalars(select(Pet).where(Pet.status == Status.available))
            pets = result.all()

            resp_msg = GetAllPetsResponse(pets=[PetModel.model_validate(pet) for pet in pets], headers=msg.headers)
            await self.send_message(resp_msg)

    @handle(GetPetById)
    async def get_pet_by_id(self, msg: GetPetById) -> None:
        async with session_local() as session:
            stmt = select(Pet).where(Pet.id == msg.id)
            result = await session.scalars(stmt)
            pet = result.scalar_one()
            resp_msg = GenericPetResponse(pet=PetModel.model_validate(pet))
            await self.send_message(resp_msg)

    @handle(UpdatePetStatusById)
    async def update_pet_status_by_id(self, msg: UpdatePetStatusById) -> None:
        async with session_local() as session:
            stmt = update(Pet).where(Pet.id == msg.id).values(status=msg.status).returning(Pet)

            result = await session.execute(stmt)
            pet = result.scalar_one()

            await session.commit()
            resp_msg = GenericPetResponse(pet=PetModel.model_validate(pet))
            await self.send_message(resp_msg)

    @handle(CreatePet)
    async def add_pet(self, msg: CreatePet) -> None:
        async with session_local() as session:
            stmt = insert(Pet).values(
                    name=msg.name,
                    image=msg.image,
                    species=msg.species,
                    description=msg.description,
                ).returning(Pet)

            result = await session.execute(stmt)
            pet = result.scalar_one()
            await session.commit()

            resp_msg = GenericPetResponse(pet=PetModel.model_validate(pet))
            await self.send_message(resp_msg)

    @handle(DeletePetById)
    async def delete_pet_by_id(self, msg: DeletePetById) -> None:
        async with session_local() as session:
            stmt = delete(Pet).where(Pet.id == msg.id).returning(Pet.id)
            result = await session.execute(stmt)
            pet_id = result.scalar_one_or_none()
            if pet_id is None:
                resp_msg = DeletePetResponse(id=msg.id, success=False)
            else:
                await session.commit()
                resp_msg = DeletePetResponse(id=pet_id, success=True)
            await self.send_message(resp_msg)