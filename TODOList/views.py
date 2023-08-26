
from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

def addtask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.isCompleted = True
    task.save()
    return redirect('home')

def undo(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.isCompleted=False
    task.save()
    return redirect('home')

def edit(request, pk):
    task=get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task=request.POST['task']
        task.task=new_task
        task.save()
        return redirect('home')
    else:
        context = {
            'task': task
        }
    return render(request, 'edit.html', context)

def delete(request, pk):
    task=get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')
