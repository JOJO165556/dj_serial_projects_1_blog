from django.test import TestCase
from django.urls import reverse
from apps.users.models import User
from apps.blog.models import Post
from apps.tags.models import Tag

class BlogCRUDTests(TestCase):
    def setUp(self):
        # Création d'un utilisateur et d'un post de test
        self.user = User.objects.create_user(username='testuser', password='password')
        self.other_user = User.objects.create_user(username='other', password='password')
        self.tag = Tag.objects.create(name='python')
        self.post = Post.objects.create(title='Test Post', content='Content', author=self.user)
        self.post.tags.add(self.tag)

    def test_post_list(self):
        """Vérifie que la liste des posts s'affiche correctement."""
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_create(self):
        """Vérifie la création d'un post avec des tags."""
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('post_create'), {
            'title': 'New Post',
            'content': 'New Content',
            'tag_input': 'django, web'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title='New Post').exists())
        post = Post.objects.get(title='New Post')
        self.assertEqual(post.tags.count(), 2)
        self.assertEqual(post.author, self.user)

    def test_post_update(self):
        """Vérifie la modification d'un post par son auteur."""
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('post_update', args=[self.post.id]), {
            'title': 'Updated Post',
            'content': 'Updated Content',
            'tag_input': 'python, update'
        })
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Post')
        self.assertEqual(self.post.tags.count(), 2)

    def test_post_delete(self):
        """Vérifie la suppression d'un post par son auteur."""
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('post_delete', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(id=self.post.id).exists())

    def test_post_update_forbidden(self):
        """Vérifie qu'un autre utilisateur ne peut pas modifier un post qui ne lui appartient pas."""
        self.client.login(username='other', password='password')
        response = self.client.post(reverse('post_update', args=[self.post.id]), {
            'title': 'Hacked Post',
            'content': 'Hacked Content',
            'tag_input': 'hack'
        })
        # Redirection vers post_detail sans modification
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertNotEqual(self.post.title, 'Hacked Post')
