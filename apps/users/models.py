# modele utilisateur custom avec role
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES =  (
        ("admin", "Admin"),
        ("author", "Author"),
        ("reader", "Reader"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="reader")