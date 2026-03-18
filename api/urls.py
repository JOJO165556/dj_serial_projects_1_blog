from rest_framework.routers import DefaultRouter
from api.views.post_views import PostViewSet
from api.views.comment_views import CommentViewSet
from api.views.tag_views import TagViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = router.urls