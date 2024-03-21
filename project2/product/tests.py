import imp
from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTest(TestCase):
    def setUp(self):
        self.product=Product.pm.create(Pro_name="TestProduct",Pro_desc="Testing product",Pro_brand="Test brand",Pro_price=200)


    def test_create_product(self):
        product=Product.pm.get(Pro_name="TestProduct")
        self.assertEqual(product.id,self.product.id)

    def test_Update(self):
        product=Product.pm.get(Pro_name="TestProduct")
        oldprice=product.Pro_price
        product.Pro_price=700
        product.save()

        product=Product.pm.get(Pro_name="TestProduct")
        self.assertNotEqual(oldprice,product.Pro_price)

    def test_fetech_product(self):
        products=Product.pm.all()
        count=len(products)
        self.assertGreater(count,0)

