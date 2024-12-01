from flask import Blueprint
from importlib.resources import Resource

products_bp = Blueprint("products", __name__)

# Liste fictive de produits financiers
PRODUCTS = [
    {"symbol": "AAPL", "name": "Apple Inc.", "category": "stock"},
    {"symbol": "GOOGL", "name": "Alphabet Inc.", "category": "stock"},
    {"symbol": "EURUSD", "name": "Euro / US Dollar", "category": "currency"},
    {"symbol": "XAUUSD", "name": "Gold", "category": "commodity"},
    {"symbol": "BTCUSD", "name": "Bitcoin", "category": "cryptocurrency"},
]


class ProductList(Resource):
    def get(self):
        """Récupère la liste des produits financiers disponibles."""
        return {"products": PRODUCTS}, 200


products_controller = ProductList()


@products_bp.route("/products", methods=["GET"])
def products():
    return products_controller.get()
