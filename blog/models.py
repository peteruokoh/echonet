from django.db import models
# from django.utils.text import slugify
# from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model() # This is referencing the default user model

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    video = models.FileField(upload_to="videos/", blank=True, null=True)
    publishDate = models.DateTimeField()

    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    commentDate = models.DateTimeField()

    def __str__(self):
        return f"Comment by {self.user.username}"

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")

    class Meta:
        unique_together = ('post', 'user')  # Prevent duplicate likes