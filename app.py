from flask import Flask
from flask_cors import CORS
from routes.product_routes import products_router

app = Flask(__name__)
app.register_blueprint(products_router)

CORS(app, resources={r"/*": {"origins": "*"}})

if __name__ == '__main__':
    app.run(debug=True)
