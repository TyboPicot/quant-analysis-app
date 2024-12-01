def test_get_strategies(client):
    response = client.get("/strategies")
    assert response.status_code == 200
    assert "strategies" in response.json
    assert isinstance(response.json["strategies"], list)

    # Vérification d'une stratégie spécifique
    strategies = response.json["strategies"]
    assert any(s["id"] == "moving_average" for s in strategies)