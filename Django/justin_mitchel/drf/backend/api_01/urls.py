from django.urls import path

from . import views
urlpatterns = [
  path('01/', views.api_home_01, name='api_01_home_01'), # localhost:8000/api_01/
  path('02/', views.api_home_02, name='api_01_home_02')
]