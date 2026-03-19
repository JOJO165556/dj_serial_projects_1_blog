# vues commentaires (ajout et suppression)
from django.shortcuts import redirect, get_object_or_404
from apps.blog.models import Post
from apps.comments.models import Comment
from django.contrib.auth.decorators import login_required

# ajouter un commentaire a un post
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        content = request.POST.get('content')
        
        if content:
            Comment.objects.create(
                post=post,
                author=request.user,
                content=content
            )
    return redirect('post_detail', pk=post_id)

# supprimer un commentaire (auteur ou staff seulement)
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    if request.user == comment.author or request.user.is_staff:
        comment.delete()
        
    return redirect('post_detail', pk=comment.post.id)