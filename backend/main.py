from flask import Flask
from flask_restx import Api
from flask_cors import CORS

# Initialisation de l'application Flask
app = Flask(__name__)
CORS(app)  # Autorise les requêtes cross-origin
api = Api(app, title="Quantitative Analysis API", version="1.0", description="API for quantitative trading strategies")

# Import des namespaces
from app.controllers.healthcheck import healthcheck_ns
from app.controllers.strategies import strategies_ns
from app.controllers.analyze import analyze_ns
from app.controllers.products import products_ns

# Ajout des namespaces à l'API
api.add_namespace(healthcheck_ns, path="/healthcheck")
api.add_namespace(strategies_ns, path="/strategies")
api.add_namespace(analyze_ns, path="/analyze")
api.add_namespace(products_ns, path="/products")

# Healthcheck route
@api.route('/healthcheck')
class HealthCheck:
    def get(self):
        return {"status": "OK"}, 200

if __name__ == "__main__":
    app.run(debug=True)
