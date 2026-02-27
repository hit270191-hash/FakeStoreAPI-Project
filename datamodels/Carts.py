from dataclasses import dataclass
import datetime
from datamodels.CartProduct import CartProduct


@dataclass
class Carts:
    userId: int
    date: str
    products: list[CartProduct]



