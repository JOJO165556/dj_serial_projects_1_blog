# vues tags (liste des tags + posts par tag)
from django.shortcuts import render, get_object_or_404
from apps.tags.models import Tag
from apps.blog.models import Post

# affiche tous les tags
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags/tag_list.html', {'tags': tags})

# affiche les posts filtres par un tag
def posts_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    posts = Post.objects.filter(tags=tag)
    
    return render(request, 'tags/tag_posts.html', {
        'tag': tag,
        'posts': posts
    })