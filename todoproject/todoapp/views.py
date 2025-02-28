from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'todoapp/index.html', {'tasks': tasks})



def task_list(request):
    return render(request, 'todoapp/task_list.html')

def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(title=title, description=description)
        return redirect('index')
    return render(request, 'todoapp/create.html')
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.completed = 'completed' in request.POST  # True if checkbox is checked, else False
        task.save()
    return redirect('task_list')

def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('index')
    return render(request, 'todoapp/update.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    return render(request, 'todoapp/delete.html', {'task': task})
