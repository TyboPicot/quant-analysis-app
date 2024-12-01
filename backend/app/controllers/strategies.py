from flask_restx import Namespace, Resource

strategies_ns = Namespace("strategies", description="List of trading strategies")

# Liste des stratégies disponibles
STRATEGIES = [
    {"id": "moving_average", "name": "Moving Averages", "type": "trend"},
    {"id": "breakout", "name": "Breakout Trading", "type": "trend"},
    {"id": "mean_reversion", "name": "Mean Reversion", "type": "contrarian"},
    {"id": "rsi_divergence", "name": "RSI Divergence", "type": "momentum"},
    {"id": "pair_trading", "name": "Pair Trading", "type": "statistical"},
]

@strategies_ns.route("/")
class StrategyList(Resource):
    def get(self):
        """Récupère la liste des stratégies disponibles."""
        return {"strategies": STRATEGIES}, 200
