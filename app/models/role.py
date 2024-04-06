from dataclasses import dataclass


@dataclass(init=False, repr=True, eq=True)
class Role:
    name: str
    description: str