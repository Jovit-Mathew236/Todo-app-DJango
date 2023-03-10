from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Todos
import time
from datetime import datetime
dt = datetime.now()

named_tuple = time.localtime()  # get struct_time
time_string = time.strftime("%H:%M", named_tuple)
date_string = time.strftime("%d/%m", named_tuple)
date_string2 = time.strftime("%m-%d", named_tuple)

# Create your views here.


def index(request):
    return render(request, 'index.html')


@login_required(login_url='/')
def todo(request):

    todos = Todos.objects.filter(user_id=request.user.id)

    if request.method == "POST":
        search = request.POST['search']
        # day = request.POST['date']
        time = request.POST['time']

        newTodo = Todos.objects.create(
            user_id=request.user.id, todo=search, time=time, status=False)
        newTodo.save()
    else:
        None

    return render(request, 'todo.html', {'todos': todos, 'time': time_string, 'date': dt.strftime('%A')+' '+date_string, 'date2': date_string2})


def todo_completed(request):

    todos = Todos.objects.filter(user_id=request.user.id)

    if request.method == "POST":
        todoid = request.POST['todo-id']
        statusState = request.POST['status']
        print(todoid,statusState)
        todoObj = Todos.objects.get(id=todoid)
        todoObj.status = statusState
        todoObj.save()
    else:
        None

    return render(request, 'todo.html', {'todos': todos, 'time': time_string, 'date': dt.strftime('%A')+' '+date_string, 'date2': date_string2})

def completed_todo(request):
    todos = Todos.objects.filter(user_id=request.user.id)
    
    return render(request, 'completedtodo.html',{'todos': todos, 'time': time_string, 'date': dt.strftime('%A')+' '+date_string, 'date2': date_string2})

def expired_todo(request):
    todos = Todos.objects.filter(user_id=request.user.id)
    
    return render(request, 'expired.html',{'todos': todos, 'time': time_string, 'date': dt.strftime('%A')+' '+date_string, 'date2': date_string2})