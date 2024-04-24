from rest_framework.test import APITestCase
from django.urls import reverse


class FoodAPITestCase(APITestCase):
    def test_food_api(self):
        url = reverse('foods')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
