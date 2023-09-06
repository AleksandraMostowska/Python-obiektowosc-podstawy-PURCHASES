from dataclasses import dataclass
from decimal import Decimal
import re
from re import Match
from typing import Self


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


# The Validator class checks whether the given line matches the pattern.
class Validator:
    @staticmethod
    def check_if_correct(line: str, pattern: str) -> Match[str] | None:
        return re.match(pattern, line)


# The Purchases class holds information about customers and their purchases.
@dataclass
class Purchases:
    customers_and_their_products: dict[Customer, dict[Product, int]]

    # The method gets data from file and checks via Validator whether text in the file has correct form.
    @classmethod
    def get_data(cls, file_name: str) -> Self:
        purchases = {}
        with open(file_name, 'r') as f:
            for line in f.readlines():
                if not Validator.check_if_correct(line, r'^([A-Z][a-z]+;){2}\d+;\d+ \[(([A-Z][a-z]+;){2}\d+)( ([A-Z][a-z]+;){2}\d+)*\]\n?$'):
                    raise ValueError('Input not correct')

                customer_data, product_data = line.strip().split(' [')
                customer_tmp = customer_data.split(';')
                customer = Customer(customer_tmp[0], customer_tmp[1], int(customer_tmp[2]), Decimal(customer_tmp[3]))

                products_info = product_data[:-1].split(' ')
                for p in products_info:
                    p_tmp = p.split(';')
                    product = Product(p_tmp[0], p_tmp[1], Decimal(p_tmp[2]))

                    if customer not in purchases:
                        purchases[customer] = {}

                    if product not in purchases[customer]:
                        purchases[customer][product] = 1
                    else:
                        purchases[customer][product] += 1

        return Purchases(purchases)


def main() -> None:
    data = Purchases.get_data('customer_and_products.txt')
    print(data)

if __name__ == '__main__':
    main()