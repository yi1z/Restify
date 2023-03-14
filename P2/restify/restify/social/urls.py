from django.urls import path
from . import views

urlpatterns = [
    path('comment/user/<int:target_id>/create/', views.UserCommentCreate.as_view(), name='comment-list'),
    path('comment/user/<int:target_id>/view/', views.UserCommentList.as_view(), name='comment-list'),
    path('comment/user/<int:target_id>/delete/<int:comment_id>/', views.UserCommentDelete.as_view(), name='comment-delete'),
    path('comment/property/<int:target_id>/create/', views.PropertyCommentCreate.as_view(), name='comment-list'),
    path('comment/property/<int:target_id>/view/', views.PropertyCommentList.as_view(), name='comment-list'),
    path('comment/property/<int:target_id>/delete/<int:comment_id>/', views.PropertyCommentDelete.as_view(), name='comment-delete'),
    path('comment/reply/<int:target_id>/create/', views.ReplyCommentCreate.as_view(), name='comment-list'),
    path('notification/view/', views.NotificationList.as_view(), name='notification-list'),
    path('comment/detail/<int:comment_id>/', views.CommentDetail.as_view(), name='comment-detail'),
]
