from rest_framework.viewsets import ModelViewSet
from apps.blog.models import Post
from api.serializers.post_serializer import PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer