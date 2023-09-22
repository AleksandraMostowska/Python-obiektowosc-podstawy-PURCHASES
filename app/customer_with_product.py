from dataclasses import dataclass
from app.customer import Customer
from app.product import Product
from typing import Self

# The CustomerWithProduct class creates pairs (customer, product) in order to help in method
# get_most_frequent_category_for_customers, so that later I can count how many times customers bought a product
# from this category and get the max from it.
@dataclass
class CustomerWithProduct:
    customer: Customer
    product: Product

    # This method converts given customer and product to class object.
    @classmethod
    def convert_to_customer_with_product(cls, c: Customer, p: Product) -> Self:
        return cls(c, p)

    # The method creates pairs (customer, product).
    @staticmethod
    def create_pairs(pairs: dict[Customer, list[Product]]) -> list[Self]:
        result = []
        for c, products in pairs.items():
            result.extend([CustomerWithProduct.convert_to_customer_with_product(c, p) for p in products])

        return result