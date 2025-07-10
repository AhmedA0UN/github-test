def test_read_product(self):
    product = ProductFactory.create()
    retrieved = Product.find(product.id)
    assert retrieved.name == product.name
