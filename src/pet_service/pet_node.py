from adoption_agency_common import BOAFastApi
from adoption_agency_common.saga_manager.saga_node import SagaNode
from pet_service.sagas.pet_saga import PetSaga
from pet_service.messages.pet_messages import GetAllPetsResponse, GenericPetResponse, DeletePetResponse
from pet_service.routers.pet_router import pet_router

handlers = [
    PetSaga
]

outgoing_messages = [
    GetAllPetsResponse,
    GenericPetResponse,
    DeletePetResponse
]

app = BOAFastApi(SagaNode(handlers=handlers, outgoing_messages=outgoing_messages))
def main():
    app.run(port=8081)

if __name__ == "__main__":
    main()