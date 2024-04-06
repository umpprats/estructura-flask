
from dataclasses import dataclass


@dataclass(init=False, repr=True, eq=True)
class UserData:
    surname: str
    phone: str
    address: str
    city: str
    country: str