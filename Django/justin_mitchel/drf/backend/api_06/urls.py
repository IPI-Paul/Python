from django.urls import path #, include
# Django Rest Framework Token Authentication =>
from rest_framework.authtoken.views import obtain_auth_token
# <= Django Rest Framework Token Authentication
# JSON WEB Token Authentication with simplejwt =>
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
  TokenVerifyView
)
# <= JSON WEB Token Authentication with simplejwt
from . import views


urlpatterns = [
  path('', views.api_home, name='api_06_home'), # localhost:8000/api_06/
  # path('products/', include('products_03.urls')), 
  path('auth/', obtain_auth_token, name='obtain_auth_token'),
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('token/verify/', TokenVerifyView.as_view(), name='token_verify')
]