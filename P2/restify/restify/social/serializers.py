from accounts.models import ThisUser
from property.models import Property
from rest_framework.serializers import ModelSerializer, CharField, IntegerField, DateField, FloatField, DateTimeField, ValidationError
from .models import Comment, Notify
import datetime as dt

class UserCommentSerializer(ModelSerializer):
    content = CharField()
    rate = IntegerField()

    class Meta:
        model = Comment
        fields = ['content', 'rate']

    def create(self, validated_data):
        commentee_user = self.context['request'].user
        validated_data['user'] = commentee_user

        # get the user
        target_id = self.context['view'].kwargs['target_id']
        try:
            target_user = ThisUser.objects.get(id=target_id)
        except ThisUser.DoesNotExist:
            raise ValidationError('User does not exist')
        
        validated_data['target_type'] = 'user'
        validated_data['target_id'] = target_id
        validated_data['reply_to'] = None
        validated_data['date'] = dt.datetime.now()

        # check if the user being commented is the user itself
        if commentee_user == target_user:
            raise ValidationError(
                {'content: You cannot comment on yourself'}
            )

        # generate a notification
        notification = Notify.objects.create(user=target_user, 
                                             content=f"{commentee_user.username} commented on your profile\n{validated_data['content']}", 
                                             date=dt.datetime.now())
        notification.save()

        return super().create(validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.username
        if instance.reply_to is None:
            representation['reply_to'] = "Not a reply"
        
        representation['date'] = instance.date

        replies = Comment.objects.filter(reply_to=instance)
        if len(replies) > 0:
            representation['replies'] = [("user: " + reply.user.username, "content: " + reply.content) for reply in replies]

        return representation
    

class PropertyCommentSerializer(ModelSerializer):
    content = CharField()
    rate = IntegerField()

    class Meta:
        model = Comment
        fields = ['content', 'rate']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user

        # get the property
        target_id = self.context['view'].kwargs['target_id']
        try:
            property = Property.objects.get(id=target_id)
        except Property.DoesNotExist:
            raise ValidationError('Property does not exist')
        
        validated_data['target_type'] = 'property'
        validated_data['target_id'] = target_id
        validated_data['reply_to'] = None
        validated_data['date'] = dt.datetime.now()

        # check if the user is the owner of the property
        if user == property.owner:
            raise ValidationError(
                {'content: You cannot comment on your own property'}
            )

        # generate a notification
        notification = Notify.objects.create(user=property.owner, 
                                             content=f"{user.username} commented on your property {property.property_name}\n{validated_data['content']}", 
                                             date=dt.datetime.now())
        notification.save()

        return super().create(validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.username
        if instance.reply_to is None:
            representation['reply_to'] = "Not a reply"
        
        representation['date'] = instance.date

        replies = Comment.objects.filter(reply_to=instance)
        if len(replies) > 0:
            representation['replies'] = [("user: " + reply.user.username, "content: " + reply.content) for reply in replies]
        return representation
    

class ReplyCommentSerializer(ModelSerializer):
    content = CharField()

    class Meta:
        model = Comment
        fields = ['content']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user

        # get the comment
        target_id = self.context['view'].kwargs['target_id']
        try:
            comment = Comment.objects.get(id=target_id)
        except Comment.DoesNotExist:
            raise ValidationError(
                {'content: Replying comment does not exist'},
            )
        
        validated_data['target_type'] = comment.target_type
        validated_data['target_id'] = target_id
        validated_data['reply_to'] = comment
        validated_data['date'] = dt.datetime.now()

        if comment.target_type == 'property':
            property = Property.objects.get(id=comment.target_id)

            # if the comment is made to a property
            if user != property.owner:
            
                # if the comment being replied is not done by the host of the property
                # then the user cannot reply to it
                if comment.user != property.owner:
                    raise ValidationError(
                        {'content: You cannot reply to a comment not posted by the host.'}
                    )
                
                # then only the host can reply to it
                raise ValidationError(
                    {'content: You are not the host of the property. You cannot add more replies to this comment.'}
                )
            
        # generate a notification
        notification = Notify.objects.create(user=comment.user,
                                             content=f"{user.username} replied to your comment \n'{validated_data['content']}'",
                                             date=dt.datetime.now())
        notification.save()

        return super().create(validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.username
        representation['reply_to'] = instance.reply_to.id
        return representation
    

class NotificationSerializer(ModelSerializer):
    content = CharField()
    date = DateTimeField()

    class Meta:
        model = Notify
        fields = ['content', 'date']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['date'] = instance.date

        # change the is_read status to True
        instance.is_read = True
        instance.save()
        representation['is_read'] = instance.is_read
        return representation


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['content', 'rate', 'reply_to', 'date', 'target_type', 'target_id']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.username
        representation['date'] = instance.date
        return representation

