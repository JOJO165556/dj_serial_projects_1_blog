from django.test import TestCase
from django.urls import reverse
from apps.users.models import User

class UserAuthTests(TestCase):
    def test_registration(self):
        """Vérifie l'inscription d'un nouvel utilisateur."""
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'email': 'new@test.com',
            'password1': 'StrongP@ssw0rd2026!',
            'password2': 'StrongP@ssw0rd2026!',
        })
        self.assertEqual(response.status_code, 302)  # Redirection après succès
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login(self):
        """Vérifie la connexion d'un utilisateur existant."""
        User.objects.create_user(username='testuser', password='password')
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 302)  # Redirection après succès
        # Vérifie qu'il est connecté en faisant une requête vers le profil/post_list
        response2 = self.client.get(reverse('post_list'))
        self.assertEqual(response2.status_code, 200)
