from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def signupView(rquest):
    
    
    context = {
        'form': UserCreationForm
    }
    
    return render(rquest, 'users/signup.html', context)
