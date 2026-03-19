# urls principales du projet
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.blog.urls')),
    path('users/', include('apps.users.urls')),
    path('tags/', include('apps.tags.urls')),
    path('comments/', include('apps.comments.urls')),
    path('api/', include('api.urls')), 
]
