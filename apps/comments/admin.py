from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    pass