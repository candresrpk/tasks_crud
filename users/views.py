from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.


def signupView(request):
    
    
    context = {
        'form': UserCreationForm
    }
    
    if request.method == 'GET':
        
        return render(request, 'users/signup.html', context)    
        
    else:
        
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], 
                    password=request.POST['password1']
                )
                
                user.save()
                
                return redirect('tasks:index')
            except Exception as e:
                context['message'] = str(e)
                return render(request, 'users/signup.html', context)
            
        context['message'] = 'Error password does not match'
        return render(request, 'users/signup.html', context)
