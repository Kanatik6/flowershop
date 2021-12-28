import json

from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
client = Client()
User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        self.user_1 = User.objects.create(email='saadatssu@gmail.com', password='12345678s')

    def test_registration(self):
        url = reverse('users-list')
        data = {'email': 'saadattsoft@gmail.com', 'password': '12345678s', 'password_repeat': '12345678s'}
        response = client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    # def test_user_login(self):
    #     url = reverse('token_obtain_pair')
    #     data = {'email': 'saadatssu@gmail.com', 'password': '12345678s'}
    #     response = client.post(url, json.dumps(data), content_type='application/json')
    #     self.assertEqual(response.status_code, 200)
