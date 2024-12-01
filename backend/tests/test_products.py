from main import app

def test_products():
    with app.test_client() as client:
        response = client.get('/products')
        assert response.status_code == 200
        data = response.json
        assert "products" in data
        assert len(data["products"]) > 0

        # Vérification de la structure des produits
        product = data["products"][0]
        assert "symbol" in product
        assert "name" in product
        assert "category" in product
