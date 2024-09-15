from .repository import get_all_products, create_product, get_product


def fetch_all_products():
    products = get_all_products()
    return products


def add_product(id, name, description, price):
    create_product(id, name, description, price)
    return


def fetch_product(id):
    product = get_product(id)
    return product
