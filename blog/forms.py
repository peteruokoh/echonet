from django import forms
from .models import Post, Comment, Like

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body", "image", "video"]
        widgets = {
            "title": forms.TextInput(attrs={'size': 40})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        widgets = {
            "body": forms.Textarea(attrs={"rows": 4, 'cols': 80, "placeholder": "Write a comment..."})
        }