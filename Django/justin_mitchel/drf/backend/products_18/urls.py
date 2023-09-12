from django.urls import path
from . import views
from os.path import sep

name = __file__.split(sep)[-2]


urlpatterns = [
  path('', views.product_list_create_view, name=f'api_06_{name}_list_create_view'),
  path('<int:pk>/', views.product_detail_view, name=f'api_06_{name}_detail_view'),
  path('<int:pk>/update/', views.product_update_view, name=f'api_06_{name}_edit'),
  path('<int:pk>/delete/', views.product_destroy_view, name=f'api_06_{name}_delete'), # or dest
]