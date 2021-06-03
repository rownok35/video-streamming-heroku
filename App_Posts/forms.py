from django import forms
from App_Posts.models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['thumbnil', 'caption', 'vid_url', 'catagory']


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('comment',)
