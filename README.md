# Projet Blog Django

Application de blog développée avec Django.

## Fonctionnalités
- Inscription, connexion et déconnexion.
- Création, édition et suppression de posts par leurs auteurs.
- Ajout de tags sur les posts sous forme de texte séparé par des virgules.
- Ajout de commentaires sur les posts.
- Mode clair, interface minimaliste.

## Installation et lancement

1. Créer un environnement virtuel :
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

3. Appliquer les migrations :
```bash
python manage.py migrate
```

4. Créer des données de test (optionnel) :
```bash
python manage.py seed
```
Cette commande crée 4 utilisateurs, 8 tags, 10 articles et des commentaires aléatoires.

5. Démarrer le serveur de développement :
```bash
python manage.py runserver
```

## Architecture
- `apps/blog/` : Gestion des articles et de l'affichage principal.
- `apps/users/` : Gestion de l'authentification et des comptes.
- `apps/tags/` : Gestion des mots-clés.
- `apps/comments/` : Gestion des commentaires sur les articles.
- `tests/` : Tests unitaires de l'application.