from django.urls import path
from .views import index, task_list_json, add_task, task_list

urlpatterns = [
    path('', index, name='index'),
    path('api/tasks/', task_list_json, name='task_list_json'),
    path('add/', add_task, name='add_task'),
    path('tasks/', task_list, name='task_list'),
]
