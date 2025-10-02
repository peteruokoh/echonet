from django import forms
from .models import Post, Comment, Like

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body", "image", "video"]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your post content...'
            }),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'video': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    # Override the form's __init__ method to add autofocus to the title input without losing existing attributes
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add autofocus attribute to title field widget, preserving existing attrs
        self.fields['title'].widget.attrs['autofocus'] = 'autofocus'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your comment...'
            }),
        }