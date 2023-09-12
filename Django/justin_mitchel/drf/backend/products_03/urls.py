from django.urls import path
from . import views
from os.path import sep

name = __file__.split(sep)[-2]

urlpatterns = [
  path('<int:pk>/', views.product_detail_view, name=f'api_06_{name}_detail_view'),
  path('', views.product_create_view, name=f'api_06_{name}_create_view'),
]