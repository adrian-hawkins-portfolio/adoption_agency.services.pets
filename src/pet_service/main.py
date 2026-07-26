from adoption_agency_common import BOAFastApi
from pet_service.routers.pet_router import pet_router

app = BOAFastApi()
app.include_router(
    pet_router
)
def main():
    app.run()

if __name__ == "__main__":
    main()