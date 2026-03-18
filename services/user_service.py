from apps.users.models import User
from django.contrib.auth import authentificate

def create_user(data):
    return User.objects.create_user(**data)
        
def login_user(email, password):
    user = authentificate(email=email, password=password)
    if user is not None and user.is_active:
        return user
    return None

def get_user_profile(user_id):
    return User.objects.get(id=user_id)

def update_user(user, data):
    for key, value in data.items():
        setattr(user, key, value)
        
    user.save()
    return user