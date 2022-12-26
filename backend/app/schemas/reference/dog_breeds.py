from enum import Enum

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
    ROTTWEILER = "Rottweiler"
    MASTIFF = "Mastiff"
