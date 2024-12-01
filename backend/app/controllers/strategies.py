from flask import Blueprint
from importlib.resources import Resource

strategies_bp = Blueprint("strategies", __name__)

# Liste des stratégies disponibles
STRATEGIES = [
    {"id": "moving_average", "name": "Moving Averages", "type": "trend"},
    {"id": "breakout", "name": "Breakout Trading", "type": "trend"},
    {"id": "mean_reversion", "name": "Mean Reversion", "type": "contrarian"},
    {"id": "rsi_divergence", "name": "RSI Divergence", "type": "momentum"},
    {"id": "pair_trading", "name": "Pair Trading", "type": "statistical"},
]

class StrategyList(Resource):
    def get(self):
        """Récupère la liste des stratégies disponibles."""
        return {"strategies": STRATEGIES}, 200

strategies_controller = StrategyList()

@strategies_bp.route("/strategies", methods=["GET"])
def strategies():
    return strategies_controller.get()