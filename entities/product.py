from dataclasses import dataclass
from marshmallow import Schema, fields, validate, post_load


@dataclass
class Product:
    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, description={self.description}, price={self.price})>"


class ProductSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    description = fields.Str(
        required=True, validate=validate.Length(min=10, max=100))
    price = fields.Float(required=True, validate=validate.Range(min=0.01))

    @post_load
    def make_product(self, data, **kwargs):
        return Product(**data)
