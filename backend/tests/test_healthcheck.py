from main import app

def test_healthcheck():
    with app.test_client() as client:
        response = client.get('/healthcheck')
        assert response.status_code == 200
        assert response.json == {"status": "OK"}
