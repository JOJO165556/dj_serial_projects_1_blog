from apps.tags.models import Tag

def create_tag(name):
    return Tag.objects.create(name=name)

def get_all_tags():
    return Tag.objects.all()

def assign_tags_to_post(post, tags):
    post.tags.set(tags)
    post.save()
    return post