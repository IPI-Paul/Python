from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

def todo003View(request):
  all_todo_items = TodoItem.objects.all()
  return render(request, 'todo_003.html', {
    'all_items': all_todo_items
  })

def addTodo(request):
  # create a new todo all_itmes
  new_item = TodoItem(content = request.POST['content'])
  # save
  new_item.save()
  # redirect the browser to '/todo/'
  return HttpResponseRedirect('/todo_003/')

def deleteTodo(request, todo_id):
  # Retrieve todo bject using id
  item_to_delete = TodoItem.objects.get(id=todo_id)
  # delete the item from the database
  item_to_delete.delete()
  # redirect the browser to '/todo/'
  return HttpResponseRedirect('/todo_003/')
