# urls d'authentification (login, register, logout)
from django.urls import path
from .views import register_view, login_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', LogoutView.as_view(next_page='post_list'), name='logout'),
]
