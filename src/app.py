from flask import Flask
from dotenv import load_dotenv
from product.controller import product_bp
from users.controller import user_bp
load_dotenv()
app = Flask(__name__)

app.register_blueprint(blueprint=product_bp, url_prefix="/products")
app.register_blueprint(blueprint=user_bp, url_prefix="/users")

if __name__ == "__main__":
    app.run(debug=True)
