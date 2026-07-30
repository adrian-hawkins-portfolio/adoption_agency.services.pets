from adoption_agency_common import BOAFastApi
from adoption_agency_common.saga_manager.saga_node import SagaNode
from pet_service.http_sagas.pet_http_saga import PetHttpSaga
from pet_service.messages.pet_messages import GetPets
from pet_service.routers.pet_router import pet_router

handlers = [
    PetHttpSaga
]

outgoing_messages = [
    GetPets
]

app = BOAFastApi(SagaNode(handlers=handlers, outgoing_messages=outgoing_messages))
app.include_router(
    pet_router,
    prefix="/pets"
)
def main():

    app.run(port=8080)

if __name__ == "__main__":
    main()