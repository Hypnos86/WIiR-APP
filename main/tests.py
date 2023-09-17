from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from .models import Car  # Zaimportuj modele, które są używane w Twoim kodzie


class TestMainViews(TestCase):

    def setUp(self):
        # Tworzenie użytkownika do testów
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_welcome_view(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('main:welcome'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/home.html')
