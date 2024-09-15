from flask import Flask
from dotenv import load_dotenv
from product.controller import product_bp


load_dotenv()
app = Flask(__name__)

app.register_blueprint(blueprint=product_bp, url_prefix="/products")

if __name__ == "__main__":
    app.run(debug=True)
