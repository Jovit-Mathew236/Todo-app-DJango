from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('todo', views.todo),
    path('todo_completed', views.todo_completed)
]
