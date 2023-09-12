from django.urls import path
from . import views
from os.path import sep

name = __file__.split(sep)[-2]

urlpatterns = [
  path('', views.product_list_create_view, name=f'api_06_{name}_list_create_view'),
  path('01/', views.product_list_view, name=f'api_06_{name}_list_view'),
  path('02/', views.product_alt_view_01, name=f'api_06_{name}_alt_view_01'),
  path('02/<int:pk>/', views.product_alt_view_01, name=f'api_06_{name}_alt_view_02'),
  path('03/<int:pk>/', views.product_alt_view_02, name=f'api_06_{name}_alt_view_03'),
  path('<int:pk>/update/', views.product_update_view, name='product-edit'),
  path('<int:pk>/delete/', views.product_destroy_view, name='product-delete'), # or destroy
  path('mixin/', views.product_mixin_view, name='product_mixin_view_01'),
  path('mixin/<int:pk>/', views.product_mixin_view, name='product_mixin_view_02'),
]