class Product:
    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, description={self.description}, price={self.price})>"
