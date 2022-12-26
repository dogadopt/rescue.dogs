from enum import Enum
from typing import Union, List, Optional
from pydantic import BaseModel, Field

class Breed(str, Enum):
    """This is a breed of dog

    Args:
        str (_type_): _description_
        Enum (_type_): _description_
    """
    LABRADOR = "Labrador"
    STAFFORDSHIREBULLTERRIER = "Staffordshire Bull Terrier"
    GERMANSHEPHERD = "German Shepherd"
    JACKRUSSEL = "Jack Russel"

class BaseDog(BaseModel):
    """This is a dog

    Args:
        BaseModel (_type_): _description_
    """
    name: str = Field(example="Mika"
                      ,description="This is the name of the dog")
    breed: Union[List[Breed], None] = Field(default=None
                                                ,example=["Jack Russel"]
                                                ,description="These are the breeds \
                                                of the dog")

class CreateRescueDog(BaseDog):
    """_summary_

    Args:
        BaseDog (_type_): _description_
    """
    rescue_name: str = Field(example="Hope Rescue"
                             ,description="This is the name of the dog rescue")
