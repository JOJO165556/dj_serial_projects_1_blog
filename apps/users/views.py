# vues d'authentification (inscription + connexion)
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

# inscription d'un nouvel utilisateur
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = RegisterForm()
        
    return render(request, 'users/register.html', {'form': form})

# connexion d'un utilisateur existant
def login_view(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('post_list')
    else:
        form = AuthenticationForm()
            
    return render(request, 'users/login.html',{'form': form})