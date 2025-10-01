from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from .validators import validate_image_size, validate_video_size

# Create your models here.
User = get_user_model() # This is referencing the default user model

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to="images/", validators=[
            validate_image_size,
            FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])
        ], help_text='Only JPG, JPEG, PNG files allowed. Max size: 1 MB.', blank=True, null=True)
    video = models.FileField(upload_to="videos/", validators=[
            validate_video_size,
            FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'avi'])
        ], help_text='Only MP4, MOV, AVI files allowed. Max size: 10 MB.', blank=True, null=True)
    publishDate = models.DateTimeField()

    def total_likes(self):
        return self.likes.count()
    
    def total_comments(self):
        return self.comments.count()
    
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