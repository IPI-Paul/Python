from django.urls import path #, include
from . import views


urlpatterns = [
  path('01/', views.api_home_01, name='api_05_home_01'), # localhost:8000/api_05/
  path('02/', views.api_home_02, name='api_05_home_02'), 
  path('03/', views.api_home_03, name='api_05_home_03'), 
  path('04/', views.api_home_04, name='api_05_home_04'), 
]