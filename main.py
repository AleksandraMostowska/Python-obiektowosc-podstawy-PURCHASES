from app.purchases import Purchases

def main() -> None:
    data = Purchases.get_data('data/customer_and_products.txt')
    print(data)

    print(f'Customers who spent the most: {data.get_customers_who_spent_the_most()}')

    category = 'Jedzenie'
    print(f'Customers who spent the most in category: {data.get_most_spending_in_category(category)}')

    print(f'Age and category: {data.get_age_and_category()}')

    print(f'Average price in category: {data.get_average_price_and_category()}')

    print(f'Most and least expensive products: {data.get_most_and_least_expensive_in_category()}')

    print(f'Customers and their most frequent category: {data.get_most_frequent_category_for_customers()}')

    print(f'Can customer pay? {data.can_customer_pay()}')

if __name__ == '__main__':
    main()