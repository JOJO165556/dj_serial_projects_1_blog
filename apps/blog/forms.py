# formulaire pour creer/modifier un post
from django import forms
from .models import Post
from apps.tags.models import Tag

class PostForm(forms.ModelForm):
    # champ texte pour taper les tags separés par des virgules
    tag_input = forms.CharField(
        required=False,
        label='Tags',
        help_text='Sépare les tags par des virgules, ex: python, django, web',
        widget=forms.TextInput(attrs={'placeholder': 'python, django, web'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # pre-remplir le champ avec les tags existants du post
        if self.instance.pk:
            self.fields['tag_input'].initial = ', '.join(
                tag.name for tag in self.instance.tags.all()
            )

    def save(self, commit=True):
        post = super().save(commit=commit)
        if commit:
            self._save_tags(post)
        return post

    def _save_tags(self, post):
        # on vide les anciens tags et on recree depuis le champ texte
        tag_names = [t.strip().lower() for t in self.cleaned_data['tag_input'].split(',') if t.strip()]
        post.tags.clear()
        for name in tag_names:
            tag, _ = Tag.objects.get_or_create(name=name)
            post.tags.add(tag)