# vues du blog (CRUD posts)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm

# page d'accueil, affiche les 3 derniers posts
def home(request):
    posts = Post.objects.select_related('author').prefetch_related('tags').all()[:3]
    return render(request, 'blog/home.html', {'posts': posts})

# liste de tous les posts, tri par date decroissante
@login_required
def post_list(request):
    posts = Post.objects.select_related('author').prefetch_related('tags').all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

# detail d'un post avec ses commentaires
def post_detail(request, pk):
    post = get_object_or_404(Post.objects.select_related('author').prefetch_related('tags', 'comments__author'), pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# creation d'un post, on assigne l'auteur automatiquement
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form._save_tags(post)
            messages.success(request, 'Post créé avec succès !')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form})


# modification d'un post, seul l'auteur ou un staff peut modifier
@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user and not request.user.is_staff:
        messages.error(request, "Vous n'êtes pas autorisé à modifier ce post.")
        return redirect('post_detail', pk=post.pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post mis à jour avec succès !')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {'form': form, 'post': post})


# suppression d'un post, seul l'auteur ou un staff peut supprimer
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user and not request.user.is_staff:
        messages.error(request, "Vous n'êtes pas autorisé à supprimer ce post.")
        return redirect('post_detail', pk=post.pk)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post supprimé.')
        return redirect('post_list')

    return render(request, 'blog/post_confirm_delete.html', {'post': post})