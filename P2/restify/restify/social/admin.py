from django.contrib import admin
from social.models.notify import Notify
from social.models.comment_model import Comment
# Register your models here.
admin.site.register(Notify)
admin.site.register(Comment)