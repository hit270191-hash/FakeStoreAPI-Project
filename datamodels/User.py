from dataclasses import dataclass

from datamodels.Address import Address
from datamodels.Name import Name


@dataclass
class User:
    email: str
    username: str
    password: str
    name: Name
    address: Address
    phone: str


