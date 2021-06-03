from django.contrib import admin
from App_Posts.models import Post, Like, Comment, Dislike

from embed_video.admin import AdminVideoMixin


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


# Register your models here.
# admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Dislike)
admin.site.register(Post, MyModelAdmin)
# admin.site.unregister(Post)  # First unregister the old class
