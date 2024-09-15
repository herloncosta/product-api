from .repository import get_all_products


def fetch_all_products():
    products = get_all_products()
    return products
