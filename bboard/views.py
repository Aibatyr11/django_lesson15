from django.shortcuts import render
from django.http import JsonResponse
from .models import Task

def index(request):
    return render(request, 'index.html')

def task_list_json(request):
    # List comprehension для формирования массива задач
    data = [
        {"id": task.id, "title": task.title, "completed": task.completed}
        for task in Task.objects.all()
    ]
    return JsonResponse(data, safe=False)
