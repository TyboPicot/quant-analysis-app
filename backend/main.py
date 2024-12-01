from flask import Flask
from flask_cors import CORS
# Import des blueprints
from app.controllers.healthcheck import healthcheck_bp
from app.controllers.strategies import strategies_bp
from app.controllers.analyze import analyze_bp
from app.controllers.products import products_bp

# Initialisation de l'application Flask
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)  # Autorise les requêtes cross-origin

app.register_blueprint(healthcheck_bp)
app.register_blueprint(strategies_bp)
app.register_blueprint(analyze_bp)
app.register_blueprint(products_bp)

if __name__ == '__main__':
    app.run(debug=True)
