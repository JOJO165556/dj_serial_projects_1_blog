# commande pour remplir la base avec des donnees de test
import random
from django.core.management.base import BaseCommand
from apps.users.models import User
from apps.blog.models import Post
from apps.tags.models import Tag
from apps.comments.models import Comment

class Command(BaseCommand):
    help = 'Remplit la base avec des donnees de test'

    def handle(self, *args, **kwargs):
        # creation des utilisateurs
        users = []
        for name in ['alice', 'bob', 'charlie', 'diana']:
            user, created = User.objects.get_or_create(
                username=name,
                defaults={'email': f'{name}@blog.com'}
            )
            if created:
                user.set_password('pass1234')
                user.save()
            users.append(user)
        self.stdout.write(f'{len(users)} utilisateurs prets')

        # creation des tags
        tag_names = ['python', 'django', 'javascript', 'css', 'html', 'api', 'devops', 'linux']
        tags = []
        for name in tag_names:
            tag, _ = Tag.objects.get_or_create(name=name)
            tags.append(tag)
        self.stdout.write(f'{len(tags)} tags prets')

        # creation des posts
        posts_data = [
            ('Debuter avec Django', 'Django est un framework Python puissant pour le web. Il permet de creer des applications rapidement grace a son ORM, son systeme de templates et son admin integre.'),
            ('Les bases de Python', 'Python est un langage simple et lisible. Il est utilise partout : web, data science, automatisation, IA. Apprenez les bases pour bien demarrer.'),
            ('CSS Flexbox en pratique', 'Flexbox simplifie la mise en page. Fini les galeres de centrage vertical. Un display flex et quelques proprietes suffisent.'),
            ('API REST avec Django', 'Django REST Framework permet de creer des API rapidement. Serializers, ViewSets, permissions, tout est la pour structurer votre backend.'),
            ('Git pour les debutants', 'Git est indispensable pour tout developpeur. Branches, commits, merges : comprendre les bases vous fera gagner un temps fou.'),
            ('Linux au quotidien', 'Utiliser Linux pour developper est un vrai plus. Terminal, permissions, gestion de paquets : tout est plus fluide pour le dev.'),
            ('JavaScript moderne', 'ES6 a change JavaScript : arrow functions, destructuring, async/await. Le langage est devenu bien plus agreable a utiliser.'),
            ('Deployer une app Django', 'Deployer sur un serveur Linux avec Gunicorn et Nginx, ca parait complique mais en quelques etapes c est faisable.'),
            ('HTML semantique', 'Utiliser les bonnes balises HTML (article, section, nav, main) ameliore l accessibilite et le SEO de votre site.'),
            ('Travailler avec les API', 'Consommer des API REST avec Python c est simple avec requests. Fetch en JS aussi. Voyons les bonnes pratiques.'),
        ]

        posts = []
        for title, content in posts_data:
            post, created = Post.objects.get_or_create(
                title=title,
                defaults={
                    'content': content,
                    'author': random.choice(users),
                }
            )
            if created:
                post.tags.set(random.sample(tags, k=random.randint(1, 3)))
            posts.append(post)
        self.stdout.write(f'{len(posts)} posts prets')

        # creation des commentaires
        commentaires = [
            'Super article, merci !',
            'Tres clair et utile.',
            'J aurais aime plus de details sur ce point.',
            'Exactement ce que je cherchais.',
            'Bien explique, bravo.',
            'Un peu court mais ca donne les bases.',
            'Je vais tester ca ce weekend.',
            'Merci pour le partage !',
        ]

        count = 0
        for post in posts:
            nb = random.randint(1, 4)
            for _ in range(nb):
                Comment.objects.create(
                    post=post,
                    author=random.choice(users),
                    content=random.choice(commentaires)
                )
                count += 1
        self.stdout.write(f'{count} commentaires crees')

        self.stdout.write(self.style.SUCCESS('Seeder termine.'))
