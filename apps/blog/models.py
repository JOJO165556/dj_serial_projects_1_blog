# modele Post
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    tags = models.ManyToManyField("tags.Tag", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)