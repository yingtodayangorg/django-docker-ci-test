import json
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import User


class TestUserView(APITestCase):
    def setUp(self):
        user = User(name='Test1', dni='09876543210')
        user.save()
        self.url = reverse("users-list")
        self.data = {'name': 'Test2', 'dni': '09876543211'}
        self.put_data = {'name': 'Test3', 'dni': '09876543213'}
        self.already_exists_data = {'name': 'Test1', 'dni': '09876543210'}

    def test_post(self):
        response = self.client.post(
            self.url,
            self.data,
            format='json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            json.loads(response.content),
            {"id": 2, "name": "Test2", "dni": "09876543211"}
        )
        self.assertEqual(User.objects.count(), 2)

    def test_get_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(json.loads(response.content)), 1)

    def test_get(self):
        response = self.client.get(self.url + '1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json.loads(response.content),
            {"id": 1, "name": "Test1", "dni": "09876543210"}
        )

    def test_put(self):
        response = self.client.put(
            self.url + '1/',
            self.put_data,
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json.loads(response.content),
            {"id": 1, "name": "Test3", "dni": "09876543213"}
        )

    def test_exiting_post(self):
        response = self.client.post(
            self.url,
            self.already_exists_data,
            format='json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            json.loads(response.content),
            {"detail": "User already exists"}
        )