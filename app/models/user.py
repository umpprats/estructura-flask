from dataclasses import dataclass

@dataclass(init=False, repr=True, eq=True)
class User:
    username: str
    password: str
    email: str
