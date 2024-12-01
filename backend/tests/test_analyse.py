from unittest.mock import patch

import pandas as pd


def test_post_analysis(client):
    mock_result = {
        "signals": 1500,
        "cumulative_return": 200,
        "max_drawdown": 100,
        "sharpe_ratio": 0.6,
    }
    with patch("moving_average_analysis") as mock_analysis:
        # Set up mock to return mock_data as a DataFrame
        mock_analysis.return_value = mock_result
        payload = {
            "strategy": "moving_average",
            "product_symbol": "AAPL",
            "start_date": "2018-01-01",
            "end_date": "2018-01-31",
        }
        response = client.post("/analyze", json=payload)
        assert response.status_code == 200

        # Vérification du contenu de la réponse
        assert "result" in response.json
        assert "indicators" in response.json["result"]
        assert isinstance(response.json["result"]["indicators"], dict)


def test_post_analysis_invalid_strategy(client):
    payload = {
        "strategy": "invalid_strategy",
        "product_symbol": "AAPL",
        "start_date": "2018-01-01",
        "end_date": "2018-01-31",
    }
    response = client.post("/analyze", json=payload)
    assert response.status_code == 400
    assert response.json["error"] == "Strategy not implemented"


def test_post_analysis_unsupported_product(client):
    payload = {
        "strategy": "moving_average",
        "product_symbol": "UNSUPPORTED",
        "start_date": "2018-01-01",
        "end_date": "2018-01-31",
    }
    response = client.post("/analyze", json=payload)
    assert response.status_code == 400
    assert response.json == {"error": "Unsupported product symbol"}
