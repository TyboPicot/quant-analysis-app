from flask import Blueprint, jsonify
from importlib.resources import Resource

healthcheck_bp = Blueprint("healthcheck", __name__)


@healthcheck_bp.route('/healthcheck', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok', 'message': 'Server is healthy'}), 200
