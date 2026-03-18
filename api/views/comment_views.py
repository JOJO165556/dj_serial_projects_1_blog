from rest_framework.viewsets import ModelViewSet
from apps.comments.models import Comment
from api.serializers.comment_serializer import CommentSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer