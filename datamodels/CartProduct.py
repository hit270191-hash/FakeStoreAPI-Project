from dataclasses import dataclass

from datamodels.Address import Address
from datamodels.Name import Name


@dataclass
class CartProduct:
    productId: int
    quantity: int
