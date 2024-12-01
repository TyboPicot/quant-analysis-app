import pytest
from main import app

@pytest.fixture
def client():
    """Fixture qui configure un client de test Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client