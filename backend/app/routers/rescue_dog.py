from fastapi import status, Response, APIRouter
from jsf import JSF
from ..schemas.rescue_dog import BaseDog

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