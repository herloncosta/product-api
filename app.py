from flask import Flask
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from routes.product_routes import products_router

app = Flask(__name__)
app.register_blueprint(products_router)

CORS(app, resources={r"/*": {"origins": "*"}})

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

if __name__ == '__main__':
    app.run(debug=True)
