from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem 
from django.contrib.auth.models import User

def home(request):
    
    return render(request,'todo/home.html')



def todoView(request):
    all_items = TodoItem.objects.filter(author = request.user)
    return render(request, 'todo/todo.html', {'all_items' : all_items})

def addTodo(request):
    new_item = TodoItem(author= request.user, content = request.POST['content'])
    new_item.save()

    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):

    item = TodoItem.objects.get(id = todo_id)
    item.delete()
    return HttpResponseRedirect('/todo/')
