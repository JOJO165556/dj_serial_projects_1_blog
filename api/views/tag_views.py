from rest_framework.viewsets import ModelViewSet
from apps.tags.models import Tag
from api.serializers.tag_serializer import TagSerializer

class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer