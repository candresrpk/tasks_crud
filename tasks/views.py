from django.shortcuts import render
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

    return render(request, 'tasks/create.html', context)
