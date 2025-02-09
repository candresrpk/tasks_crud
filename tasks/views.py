from django.shortcuts import render
from .models import Tasks

# Create your views here.


def HomeView(request):

    if request.user.is_authenticated:
        tasks = Tasks.objects.filter(owner=request.user)

        context = {
            'tasks': tasks
        }

    else:
        context = {}

    return render(request, 'tasks/home.html', context)
