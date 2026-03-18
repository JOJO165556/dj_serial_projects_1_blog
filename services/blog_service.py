from apps.blog.models import Post

def create_post(user, title, content, tags=[]):
    if user.role not in ["admin", "author"]:
        raise Exception("Permission refusée")
    
    post = Post.objects.create(
        author=user,
        title=title,
        content=content
    )
    
    post.tags.set(tags)
    return post
    
def update_post(user, post_id, data):
    post = Post.objects.get(id=post_id)
    
    if post.author != user and user.role != "admin":
        raise Exception("Interdit")
    
    for key, value in data.items():
        setattr(post, key, value) 
        
    post.save()
    return post
   
def delete_post(user, post_id):
    post = Post.objects.get(id=post_id)
    
    if post.author != user and user.role != "admin":
        raise Exception("Interdit")
    
    post.delete()
        
def get_post(post_id):
    return Post.objects.get(id=post_id)

def list_posts():
    return Post.objects.all().order_by("-created_at")

def search_posts(query):
    return Post.objects.filter(title__icontains=query)