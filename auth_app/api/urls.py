from django.urls import path
from .views import RegistrationView, HelloWorldView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 

    path('hello/',  HelloWorldView.as_view(), name='hello')
]
