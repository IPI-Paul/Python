from django.urls import path
from . import views

urlpatterns = [
  path('', views.api_home, name='api_04_home'), # localhost:8000/api_04/
]