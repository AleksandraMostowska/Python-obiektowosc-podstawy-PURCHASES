from dataclasses import dataclass
from decimal import Decimal
import re
from re import Match
from typing import Self, Any
from collections import defaultdict


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

    # The method gets customer's total spending.
    def get_total_customer_spent(self, customer: Customer) -> Decimal:
        total_spent = Decimal(0)

        if customer in self.customers_and_their_products:
            for product, quantity in self.customers_and_their_products[customer].items():
                total_spent += product.price * quantity
        return total_spent

    # The method gets the customer or customers who spent the most.
    def get_customers_who_spent_the_most(self) -> list[Customer]:
        customers_and_their_spent = dict([(c, self.get_total_customer_spent(c)) for c in self.customers_and_their_products.keys()])
        grouped_by_spending = defaultdict(list)
        for c in customers_and_their_spent.items():
            grouped_by_spending[c[1]].append(c[0])

        return max(grouped_by_spending.items(), key=lambda x: x[0])[1]

    # The method gets the customer or customers who spent the most in a given category.
    def get_most_spending_in_category(self, category: str) -> list[Customer]:
        customer_and_their_spent = defaultdict(list)

        for customer, products in self.customers_and_their_products.items():
            for product, quantity in products.items():
                if product.category == category:
                    customer_and_their_spent[customer].append(product.price * quantity)

        summed_spending = defaultdict(list)
        for customer, spending_list in customer_and_their_spent.items():
            summed_spending[sum(spending_list)].append(customer)

        return max(summed_spending.items(), key=lambda x: x[0])[1]

    # The method returns summary that shows the age and category from which products were most frequently
    # purchased at a given age.
    def get_age_and_category(self) -> defaultdict[int, list]:
        age_and_category = defaultdict(list)
        for customer, products in self.customers_and_their_products.items():
            for product in products:
                age_and_category[customer.age].append(product.category)

        for a, c in age_and_category.items():
            age_and_category[a] = max(set(c), key=c.count)

        return age_and_category


def main() -> None:
    data = Purchases.get_data('customer_and_products.txt')
    print(data)

    print(f'Customers who spent the most: {data.get_customers_who_spent_the_most()}')

    category = 'Jedzenie'
    print(f'Customers who spent the most in category: {data.get_most_spending_in_category(category)}')

    print(f'Age and category: {data.get_age_and_category()}')

if __name__ == '__main__':
    main()