from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment

# minimal SignUpForm (so views importing it won't fail)
class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content', '')
        if not content or len(content.strip()) == 0:
            raise forms.ValidationError("Comment cannot be empty.")
        return content
