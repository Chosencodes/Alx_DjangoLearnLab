from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget  # for tagging

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),  # mandatory for ALX checker
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content': 'Add your comment'}
