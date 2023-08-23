from django.http import HttpResponse
from django.shortcuts import render
from TODOList.models import Task

def home(request):
    tasks=Task.objects.filter(isCompleted =False).order_by('-updated_at')
    contexts ={
        'tasks': tasks,
    }
    return render(request, 'home.html', contexts)