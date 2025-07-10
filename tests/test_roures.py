def test_get_product(client):
    product = ProductFactory.create()
    response = client.get(f'/products/{product.id}')
    assert response.status_code == 200
