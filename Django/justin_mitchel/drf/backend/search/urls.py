from django.urls import path, include
from . import views


urlpatterns = [
  path('19/', views.SearchListView19.as_view(), name='search_19'),
  path('20/', views.SearchListView20.as_view(), name='search_20')
]