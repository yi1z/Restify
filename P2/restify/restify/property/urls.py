from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [ 
    path('create/', views.PorpertyCreate.as_view(), name='create'),
    path('edit/<int:property_id>/', views.PorpertyEdit.as_view(), name='edit'),
    # make a url allow the ower to create the availavility of the specific property
    path('availability/<int:property_id>/', views.AvailabilityCreate.as_view(), name='create-availability'),
]