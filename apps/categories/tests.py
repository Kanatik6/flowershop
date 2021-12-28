import json

from django.urls import reverse
from django.test import TestCase, Client

from apps.categories.models import Category
client = Client()


class CategoryTestCase(TestCase):
    def setUp(self):
        self.category_1 = Category.objects.create(title='test-1')

    def test_category_create(self):
        url = reverse('category-list')
        response = client.post(url, json.dumps({'title': 'test2'}), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_category_list(self):
        url = reverse('category-list')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_category_detail(self):
        url = reverse('category-detail', args=[self.category_1.id])
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_product_delete(self):
        url = reverse('category-detail', args=[self.category_1.id])
        response = client.delete(url)
        self.assertEqual(response.status_code, 204)
