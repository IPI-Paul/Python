from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoItem

def todo001View(request):
  head = '<head><title>Todo - Tutorial 1</title></head>'
  return HttpResponse(f'{head}Hello, this is todoView')