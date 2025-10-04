from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email")

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content")

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "placeholder": "Write your comment..."}),
        label=""
    )

    class Meta:
        model = Comment
        fields = ("content",)

    def clean_content(self):
        content = self.cleaned_data.get("content", "")
        content = content.strip()
        if len(content) < 3:
            raise forms.ValidationError("Comment is too short (min 3 characters).")
        return content
