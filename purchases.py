from dataclasses import dataclass
from decimal import Decimal


# The Customer class features data of given customer, including name, last name, age and cash.
@dataclass(frozen=True, eq=True)
class Customer:
    name: str
    last_name: str
    age: int
    cash: Decimal


# The Product class contains data about a product, including name, category and price.
@dataclass(frozen=True, eq=True)
class Product:
    name: str
    category: str
    price: Decimal

def main() -> None:
    customer = Customer('AAA', 'BBBBB', 20, 2000)
    print(customer)

    product = Product('XBOX', 'RTV AGD', '3500')
    print(product)

if __name__ == '__main__':
    main()