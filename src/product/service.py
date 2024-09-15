from .repository import get_all_products, create_product


def fetch_all_products():
    products = get_all_products()
    return products


def add_product(id, name, description, price):
    create_product(id, name, description, price)
    return
