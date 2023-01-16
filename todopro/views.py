from django.shortcuts import render
from django.http import HttpResponse
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

def todo(request):
    # return HttpResponse("<h1>hi</h1>")

    todos = Todos.objects.all()

    if request.method == "POST":
        search = request.POST['search']
        time = request.POST['time']
        todoname = 'todo'+str((len(todos)+1))

        newTodo = Todos.objects.create(todo=search, time=time, status=False)
        newTodo.save()
        # print(todoname)
        # todoname = Todos()
        # todoname.todo = search
        # todoname.time = time
        # todoname.status = False
        # todos.append(todoname)
        # print(len(todos))

    return render(request, 'todo.html', {'todos': todos, 'time': time_string, 'date': dt.strftime('%A')+' '+date_string, 'date2': date_string2})
