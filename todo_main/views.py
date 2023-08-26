from django.http import HttpResponse
from django.shortcuts import render
from TODOList.models import Task

def home(request):
    tasks=Task.objects.filter(isCompleted =False).order_by('-updated_at')
    completed_task=Task.objects.filter(isCompleted=True)
    print(completed_task)

    contexts ={
        'tasks': tasks,
        'completed_task': completed_task,
    }
    return render(request, 'home.html', contexts)

