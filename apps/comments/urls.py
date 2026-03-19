# urls commentaires
from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:post_id>/', views.add_comment, name='add_comment'),
    path('delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
