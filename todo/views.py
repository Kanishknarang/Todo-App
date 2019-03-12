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
    user= request.user
    cont = request.POST['content']
    time = request.POST['tasktime']

    if cont is not None and time is not None:
        new_item = TodoItem(author= request.user, content = request.POST['content'], tasktime = request.POST['tasktime'])
        new_item.save()

    return HttpResponseRedirect('/todo/')

def deleteTodo(request, todo_id):

    item = TodoItem.objects.get(id = todo_id)
    item.delete()
    return HttpResponseRedirect('/todo/')


def updateView(request, todo_id):
    
    return render(request, 'todo/update.html', {'todo_id' : todo_id})


def updateTodo(request, todo_id):
    user= request.user
    cont = request.POST['content']
    time = request.POST['tasktime']

    item = TodoItem.objects.get(id = todo_id)
    item.content = cont
    item.tasktime = time
    item.save()
    

    return HttpResponseRedirect('/todo/')