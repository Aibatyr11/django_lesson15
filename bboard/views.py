from django.http import JsonResponse
from .models import Task
from django.shortcuts import render, redirect
from django.http import Http404
from .forms import TaskForm


def index(request):
    return render(request, 'index.html')

def task_list_json(request):
    data = [
        {"id": task.id, "title": task.title, "completed": task.completed}
        for task in Task.objects.all()
    ]
    return JsonResponse(data, safe=False)



def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tasks/')
        else:
            raise Http404("Неверные данные!")

    form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})
