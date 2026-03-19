from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Post

@admin.register(Post)
class PostAdmin(ModelAdmin):
    pass