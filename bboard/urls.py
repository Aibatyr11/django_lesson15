from django.urls import path
from .views import index, task_list_json

urlpatterns = [
    path('', index, name='index'),
    path('api/tasks/', task_list_json, name='task_list_json'),
]
