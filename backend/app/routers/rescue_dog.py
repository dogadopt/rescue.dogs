from fastapi import status, Response, APIRouter,Request
from fastapi.encoders import jsonable_encoder
from jsf import JSF
from ..schemas.rescue_dog import BaseDog
from typing import List

router = APIRouter(
    prefix="/dogs",
    tags=["dogs"]
)

@router.get("/examples")
async def example_dogs(response: Response):
    """Returns example dogs

    Returns:
        list[Beer]: Returns a list of beer objects
    """
    response.status_code=status.HTTP_200_OK
    schema = BaseDog.schema()
    faker = JSF(schema=schema)
    result = faker.generate()

    return result

@router.get("/", response_description="List of all dogs", response_model=List[BaseDog])
async def get_dogs(request: Request):
    dogs = [dog for dog in request.app.container.read_all_items()]
    return dogs

@router.get("/{id}")
async def get_dog(request: Request, id: str):
    dog = request.app.container.read_item(id, partition_key=id)
    return dog

@router.post("/", response_model=BaseDog)
async def create_dog(request: Request, dog: BaseDog):
    dog_item = jsonable_encoder(dog)
    new_dog = request.app.container.create_item(dog_item)
    return new_dog

@router.delete("/{id}")
async def delete_dog(request: Request, id: str):
    request.app.container.delete_item(id, partition_key=id)
