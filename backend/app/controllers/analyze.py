from importlib.resources import Resource
from flask import request, Blueprint
from app.services.analysis_service import moving_average_analysis

analyze_bp = Blueprint("analyze", __name__)


class Analyze(Resource):
    def post(self):
        """Lance une analyse quantitative pour un produit financier donné."""
        data = request.get_json()

        # Extraction des paramètres
        ticker = data.get("ticker")
        strategy = data.get("strategy")
        start_date = data.get("start_date")
        end_date = data.get("end_date")

        # Vérification de la stratégie
        if strategy == "moving_average":
            result = moving_average_analysis(ticker, start_date, end_date)
            return result, 200

        return {"error": "Strategy not implemented"}, 400

analyse_controller = Analyze()

@analyze_bp.route("/analyze", methods=["POST"])
def analyze():
    return analyse_controller.post()