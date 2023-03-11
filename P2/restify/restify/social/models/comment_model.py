from django.db import models
from accounts.models.user_model import ThisUser

# Create your models here.

# comments
class Comment(models.Model):
    # the user who commented
    user = models.ForeignKey(ThisUser, on_delete=models.CASCADE)
    # note: we will access the target by using the target_type and target_id
    # the type of the target being commented on
    target_type = models.CharField(max_length=20)
    # the id of the target being commented on
    target_id = models.IntegerField()
    # the content can be blank
    content = models.CharField(max_length=1000, blank=True)
    # a comment can have no rate
    rate = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    # if this comment is a reply to another comment
    # note: set to be null if not a reply
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)