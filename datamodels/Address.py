from dataclasses import dataclass
from datamodels.Geolocation import Geolocation

@dataclass
class Address:
    city: str
    street: str
    number: int
    zip_code: str
    geolocation: Geolocation