from django.urls import path
from . import views
from os.path import sep

name = __file__.split(sep)[-2]

urlpatterns = [
  path('', views.product_list_create_view, name=f'api_06_{name}_list_create_view'),
  path('<int:pk>/', views.product_detail_view, name=f'api_06_{name}_detail_view'),
  path('01/', views.product_list_create_view_01, name=f'api_06_{name}_list_create_view_01'),
  path('02/', views.product_list_create_view_02, name=f'api_06_{name}_list_create_view_02'),
  path('02/', views.product_list_create_view_02, name=f'api_06_{name}_list_create_view_03'),
  path('<int:pk>/update/', views.product_update_view, name=f'api_06_{name}_edit'),
  path('<int:pk>/delete/', views.product_destroy_view, name=f'api_06_{name}_delete'),
]