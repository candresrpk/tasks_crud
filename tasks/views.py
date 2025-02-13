from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.


def HomeView(request):

    if request.user.is_authenticated:
        tasks = Task.objects.filter(owner=request.user)

        context = {
            'tasks': tasks
        }

    else:
        context = {}

    return render(request, 'tasks/home.html', context)


def createTask(request):

    context = {
        'form': TaskForm
    }

    if request.method == 'GET':
        return render(request, 'tasks/create.html', context)

    else:
        try:
            form = TaskForm(request.POST)
            if form.is_valid():
                new_task = form.save(commit=False)
                new_task.owner = request.user
                new_task.save()
            else:
                context['form'] = form
                return render(request, 'tasks/create.html', context)
        except Exception as e:
            context['message'] = e
            return render(request, 'tasks/create.html', context)

        return redirect('tasks:home')


def updateTask(request, id):
    context = {}
    try:
        task = get_object_or_404(Task, id=id, owner=request.user)
    except Exception as e:
        return redirect('tasks:home')

    form = TaskForm(instance=task)
    context['form'] = form

    if request.method == 'GET':

        return render(request, 'tasks/update.html', context)

    else:
        try:
            new_task = TaskForm(request.POST, instance=task)
            new_task.save()

            return redirect('tasks:home')

        except Exception as e:
            context['message'] = e
            return render(request, 'tasks/update.html', context)
