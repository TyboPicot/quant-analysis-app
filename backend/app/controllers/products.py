from flask_restx import Namespace, Resource

products_ns = Namespace("products", description="List of available financial products")

# Liste fictive de produits financiers
PRODUCTS = [
    {"symbol": "AAPL", "name": "Apple Inc.", "category": "stock"},
    {"symbol": "GOOGL", "name": "Alphabet Inc.", "category": "stock"},
    {"symbol": "EURUSD", "name": "Euro / US Dollar", "category": "currency"},
    {"symbol": "XAUUSD", "name": "Gold", "category": "commodity"},
    {"symbol": "BTCUSD", "name": "Bitcoin", "category": "cryptocurrency"},
]

@products_ns.route("/")
class ProductList(Resource):
    def get(self):
        """Récupère la liste des produits financiers disponibles."""
        return {"products": PRODUCTS}, 200
