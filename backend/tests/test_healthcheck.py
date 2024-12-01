def test_healthcheck(client):
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json == {'message': 'Server is healthy', 'status': 'ok'}
