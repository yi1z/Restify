from django.shortcuts import render
from .serializers import UserCommentSerializer, PropertyCommentSerializer, ReplyCommentSerializer, NotificationSerializer, CommentSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Comment, Notify

# Create your views here.

class UserCommentCreate(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserCommentSerializer


class UserCommentList(ListAPIView):
    serializer_class = UserCommentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['date']
    search_fields = ['content']

    def get_queryset(self):
        return Comment.objects.filter(target_type='user', target_id=self.kwargs['target_id'])
    

class UserCommentDelete(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserCommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(target_type='user',
                                      target_id=self.kwargs['target_id'], 
                                      id=self.kwargs['comment_id'])

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user == request.user:
            self.perform_destroy(instance)
            return Response(status=204)
        else:
            raise PermissionDenied
            
class PropertyCommentCreate(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PropertyCommentSerializer

class PropertyCommentList(ListAPIView):
    serializer_class = PropertyCommentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['date']
    search_fields = ['content']

    def get_queryset(self):
        return Comment.objects.filter(target_type='property', target_id=self.kwargs['target_id'])
    
class PropertyCommentDelete(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PropertyCommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(target_type='property',
                                      target_id=self.kwargs['target_id'], 
                                      id=self.kwargs['comment_id'])

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user == request.user:
            self.perform_destroy(instance)
            return Response(status=204)
        else:
            raise PermissionDenied
        
class ReplyCommentCreate(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReplyCommentSerializer
        

class ReplyCommentList(ListAPIView):
    serializer_class = ReplyCommentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ['date']
    search_fields = ['content']

    def get_queryset(self):
        return Comment.objects.filter(reply_to=self.kwargs['comment_id'])

class ReplyCommentDelete(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ReplyCommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(reply_to=self.kwargs['comment_id'])

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user == request.user:
            self.perform_destroy(instance)
            return Response(status=204)
        else:
            raise PermissionDenied

class NotificationList(ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notify.objects.filter(user=self.request.user)
    

class CommentDetail(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(id=self.kwargs['comment_id'])
