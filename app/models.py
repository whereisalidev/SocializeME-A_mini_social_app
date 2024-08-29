from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pic/', blank=True)
    bio = models.TextField(max_length=160, blank=True, null=True)
    cover_pic = models.ImageField(upload_to='cover_pic/', blank=True)

    def __str__(self):
        return self.username
    

class Post(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    post_content = models.TextField(max_length=150, blank=True)
    post_image = models.ImageField(upload_to='posts/', blank=True)
    comment_count = models.IntegerField(default=0)
    creater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    saved = models.ManyToManyField(User, blank=True, related_name='saved')

    def __str__(self):
        return f"Post ID: {self.id} (creater: {self.creater})"

    def img_url(self):
        return self.post_image.url

    def append(self, name, value):
        self.name = value


class Comment(models.Model):
    comment_content = models.TextField(max_length=90)
    date_created = models.DateTimeField(auto_now_add=True)
    comments = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return f"Comment: {self.comments} | Commenter: {self.user}"


class Follower_Following(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ManyToManyField(User, blank=True, related_name='following')

    def __str__(self):
        return f"User: {self.follower}"
