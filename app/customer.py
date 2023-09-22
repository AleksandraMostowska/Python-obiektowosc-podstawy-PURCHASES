from dataclasses import dataclass
from decimal import Decimal

# The Customer class features data of given customer, including name, last name, age and cash.
@dataclass(frozen=True, eq=True)
class Customer:
    name: str
    last_name: str
    age: int
    cash: Decimal