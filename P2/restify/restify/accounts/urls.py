from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [ 
    path('create/', views.UserCreate.as_view(), name='create'),
    path('edit/<int:pk>/', views.UserEdit.as_view(), name='edit'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reservation/list/', views.ListReservation.as_view(), name='ListReservation'),
    path('reservation/list/<str:type_user>/', views.ListReservationFilterView.as_view(), name='ListReservationFilterView'),
    path('reservation/list/<str:type_user>/<str:state>/', views.ListReservationStateFilterView.as_view(), name='ListReservationStateFilterView'),
    path('reservation/list/<str:type_user>/<str:state>/<int:pk>/', views.ListReservationStateFilterView.as_view(), name='ListReservationStateFilterView'),
    path('reservation/list/<str:type_user>/<str:state>/<str:action>/', views.DetailReservationStateUpdateView.as_view(), name='DetailReservationStateUpdateView'),

]