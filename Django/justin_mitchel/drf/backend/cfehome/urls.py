"""
URL configuration for cfehome project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from index.views import ListViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListViews),
    path('api_01/', include('api_01.urls')), # localhost:8000/api_01
    path('api_02/', include('api_02.urls')), 
    path('api_03/', include('api_03.urls')), 
    path('api_04/', include('api_04.urls')), 
    path('api_05/', include('api_05.urls')), 
    path('api_06/', include('api_06.urls')), 
    path('api_06/products_03/', include('products_03.urls')),
    path('api_06/products_04/', include('products_04.urls')),
    path('api_06/products_05/', include('products_05.urls')),
    path('api_06/products_06/', include('products_06.urls')),
    path('api_06/products_07/', include('products_07.urls')),
    path('api_06/products_08/', include('products_08.urls')),
    path('api_06/products_09/', include('products_09.urls')),
    path('api_06/products_10/', include('products_10.urls')),
    path('api_06/products_11/', include('products_11.urls')),
    path('api_06/products_12/', include('products_12.urls')),
    path('api_06/products_13/', include('products_13.urls')),
    path('api_06/products_14/', include('products_14.urls')),
    path('api_06/products_15/', include('products_15.urls')),
    path('api_06/products_16/', include('products_16.urls')),
    path('api_06/products_17/', include('products_17.urls')),
    path('api_06/products_18/', include('products_18.urls')),
    path('api_06/products_19/', include('products_19.urls')),
    path('api_06/products_20/', include('products_20.urls')),
    path('api_06/v2/', include('cfehome.routers')),
    path('api_06/search/', include('search.urls'))
]
