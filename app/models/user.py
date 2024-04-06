from dataclasses import dataclass
from .user_data import UserData

@dataclass(init=False, repr=True, eq=True)
class User:
    username: str
    password: str
    email: str
    user_data: UserData
    def __init__(self, user_data: UserData = None):
        self.user_data = UserData()
