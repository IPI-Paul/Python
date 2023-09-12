from django.urls import path

from . import views
urlpatterns = [
  path('01/', views.api_home_01, name='api_02_home_01'), # localhost:8000/api_02/01
  path('02/', views.api_home_02, name='api_02_home_02'), 
  path('03/', views.api_home_03, name='api_02_home_03'), 
]