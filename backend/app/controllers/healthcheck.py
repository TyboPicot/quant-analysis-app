from flask_restx import Namespace, Resource

healthcheck_ns = Namespace("healthcheck", description="Check if the API is operational.")


@healthcheck_ns.route('/')
class HealthCheck(Resource):
    def get(self):
        """Vérifie si l'API est opérationnelle."""
        return {"status": "OK"}, 200
