"""
URL configuration for editdojo_project project.

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
from django.urls import path
from index.views import listViews
from hello.views import myView
from todo_001.views import todo001View
from todo_002.views import todo002View
from todo_003.views import todo003View, addTodo, deleteTodo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listViews),
    path('sayHello/', myView),
    path('todo_001/', todo001View),
    path('todo_002/', todo002View),
    path('todo_003/', todo003View),
    path('addTodo/', addTodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
]
