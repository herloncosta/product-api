from flask import Flask
from routes.product_routes import products_router

app = Flask(__name__)
app.register_blueprint(products_router)

if __name__ == '__main__':
    app.run(debug=True)
