from dataclasses import dataclass
from decimal import Decimal

# The Product class contains data about a product, including name, category and price.
@dataclass(frozen=True, eq=True)
class Product:
    name: str
    category: str
    price: Decimal