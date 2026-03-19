# urls tags
from django.urls import path
from . import views

urlpatterns = [
    path('', views.tag_list, name='tag_list'),
    path('<int:tag_id>/', views.posts_by_tag, name='posts_by_tag'),
]
