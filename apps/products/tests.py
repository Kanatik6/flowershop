import json

from django.test import TestCase, Client
from django.urls import reverse
# Create your tests here.
from apps.categories.models import Category
from apps.products.models import Product, ProductItem

client = Client()


class ProductTestCase(TestCase):

    def setUp(self):
        self.category = Category.objects.create(title='test1', description='test1')
        self.product = Product.objects.create(article='test1')
        self.product_item = ProductItem.objects.create(category=self.category)

    def test_product_create(self):
        url = reverse('products-list')
        response = client.post(url, json.dumps({'article': 'test'}), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_product_list(self):
        url = reverse('products-list')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_product_detail(self):
        url = reverse('products-detail', args=[self.product.id])
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_product_delete(self):
        url = reverse('products-detail', args=[self.product.id])
        response = client.delete(url)
        self.assertEqual(response.status_code, 204)

        try:
            self.product
        except:
            self.fail()

    def test_product_item_create(self):
        url = reverse('products_item-list')
        response = client.post(url, json.dumps({'category': 1}), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_product_item_list(self):
        url = reverse('products_item-list')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_product_item_detail(self):
        url = reverse('products_item-detail', args=[self.product_item.id])
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_product_item_delete(self):
        url = reverse('products_item-detail', args=[self.product_item.id])
        response = client.delete(url)
        self.assertEqual(response.status_code, 204)

        try:
            self.product_item
        except:
            self.fail()
