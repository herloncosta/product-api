from .repository import get_all_products, create_product, get_product, update_product


def fetch_all_products():
    products = get_all_products()
    return products


def add_product(id, name, description, price):
    create_product(id, name, description, price)
    return


def fetch_product(id):
    product = get_product(id)
    return product


def modify_product(product_id, name=None, description=None, price=None):
    update_product(product_id, name, description, price)
    return
