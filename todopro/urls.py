from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('todo', views.todo),
    path('todo_completed', views.todo_completed),
    path('completed_todo', views.completed_todo),
    path('expired_todo', views.expired_todo)
]