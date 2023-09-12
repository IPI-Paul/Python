from django.shortcuts import render
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import TodoItem

def todo002View(request):
  # return HttpResponse('Hello, this is todoView')
  all_todo_items = TodoItem.objects.all()
  print(request)
  return render(request, 'todo_002.html', {
    'all_items': all_todo_items
  })