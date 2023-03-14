from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [ 
    path('create/', views.UserCreate.as_view(), name='create'),

    path('edit/<int:pk>/', views.UserEdit.as_view(), name='edit'),
    #===================================================================================================
    path('reservation/create/<int:property_id>/', views.ReservationCreate.as_view(), name='ReservationCreate'),
    #===================================================================================================

    path('reservation/list/', views.ListReservation.as_view(), name='ListReservation'),

    path('reservation/list/<str:type_user>/', views.ListReservationFilterView.as_view(), name='ListReservationFilterView'),

    #change status url

    #host approve order
    path('reservation/approve/<int:order_num>/', views.ApproveReservation.as_view(), name='ApproveReservation'),
    #host/client cancel order
    path('reservation/host-cancel/<int:order_num>/', views.HostCancelReservation.as_view(), name='CancelReservation'),
    path('reservation/client-cancel/<int:order_num>/', views.ClientCancelReservation.as_view(), name='CancelReservation'),
    #host terminate order
    path('reservation/terminate/<int:order_num>/', views.TerminateReservation.as_view(), name='TerminateReservation'),
    #client denied order
    path('reservation/denied/<int:order_num>/', views.DeniedReservation.as_view(), name='DeniedReservation'),


    path('reservation/list/<str:type_user>/<str:state>/', views.ListReservationStateFilterView.as_view(), name='ListReservationStateFilterView'),


    path('reservation/list/<str:type_user>/<str:state>/<int:pk>/', views.ListReservationStateFilterView.as_view(), name='ListReservationStateFilterView'),

    
    # path('reservation/list/<str:type_user>/<str:state>/<str:action>/', views.DetailReservationStateUpdateView.as_view(), name='DetailReservationStateUpdateView'),

]