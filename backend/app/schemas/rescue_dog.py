from .reference.dog_breeds import Breed
from typing import Union, List, Optional
from pydantic import BaseModel, Field

class BaseDog(BaseModel):
    """This is a dog

    Args:
        BaseModel (_type_): _description_
    """
    id : str
    name: str = Field(example="Mika"
                      ,description="This is the name of the dog")
    breed: Union[List[Breed], None] = Field(default=None
                                                ,example=["Jack Russel"]
                                                ,description="These are the breeds \
                                                of the dog"
                                                ,max_items=3)

class CreateRescueDog(BaseDog):
    """_summary_

    Args:
        BaseDog (_type_): _description_
    """
    rescue_name: str = Field(example="Hope Rescue"
                             ,description="This is the name of the dog rescue")
