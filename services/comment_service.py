from apps.comments.models import Comment
from apps.blog.models import Post

def add_comment(user, post_id, content, parent_id=None):
    post = Post.objects.get(id=post_id)
    parent = None
    
    if parent_id:
        parent = Comment.objects.get(id=parent_id)
    
    return Comment.objects.create(
        author=user,
        post=post,
        content=content,
        parent=parent
    )
    
def update_comment(user, comment_id, content):
    comment = Comment.objects.get(id=comment_id)
    
    if comment.author != user and getattr(user, "role", None) != "admin":
        raise Exception("Interdit")
    
    comment.content = content
    comment.save()
    return comment
    
def delete_comment(user, comment_id):
    comment = Comment.objects.get(id=comment_id)
    
    if comment.author != user and user.role != "admin":
        raise Exception("Interdit")
    
    comment.delete()
def get_comments_by_post(post_id): 
    return Comment.objects.filter(post_id=post_id)