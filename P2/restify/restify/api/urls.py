from django.urls import path
from . import views
# Reference: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Delete Later: Reference: https://www.youtube.com/watch?v=xjMP0hspNLE
    # This is for testing only:
    path('', views.getTest),

    # Reference: https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html
    # This will create an endpoint to get the token.
    
    # Side Note: Access token actually is the encoded user info in the database.

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # This will create an endpoint to refresh a token.

    # Side note: refresh endpoint will take the refresh token to get the new access token. This give back us the new life token.
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
