from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post')
    # Here image is the thumbnil
    thumbnil = models.ImageField(upload_to='post_images')
    vid_url = EmbedVideoField()  # same like models.URLField()
    CHOICES = [
        ('Music', 'Music'),
        ('Science', 'Science'),
        ('Sports', 'Sports'),
        ('Game', 'Game'),
        ('Dance', 'Dance'),
        ('Others', 'Others'), ]
    catagory = models.CharField(
        max_length=264, choices=CHOICES, default='Others')

    caption = models.CharField(max_length=264, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-upload_date', ]


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='vid_comment')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_comment')

    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-comment_date',)


class Like(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='liked_post')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='liker')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} : {}'.format(self.user, self.post)


class Dislike(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='disliked_post')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='disliker')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} : {}'.format(self.user, self.post)
