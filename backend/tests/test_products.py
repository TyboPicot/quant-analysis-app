def test_get_products(client):
    response = client.get("/products")
    assert response.status_code == 200
    assert "products" in response.json
    assert isinstance(response.json["products"], list)

    # Vérification d'un produit spécifique
    products = response.json["products"]
    assert any(p["symbol"] == "AAPL" for p in products)
