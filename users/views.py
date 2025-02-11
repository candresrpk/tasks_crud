from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


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
                login(request, user)

                return redirect('tasks:index')
            except IntegrityError:
                context['message'] = 'Username already exists'
                return render(request, 'users/signup.html', context)
            except Exception as e:
                context['message'] = 'Something went wrong, please contact the administrator'
                return render(request, 'users/signup.html', context)

        context['message'] = 'Error password does not match'
        return render(request, 'users/signup.html', context)


def signinView(request):

    context = {
        'form': AuthenticationForm
    }

    if request.method == 'GET':

        return render(request, 'users/signin.html', context)

    else:
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user is not None:
            login(request, user)
            return redirect('tasks:home')
        else:
            context['message'] = 'Invalid username or password'
            return render(request, 'users/signin.html', context)


def signoutView(request):

    logout(request)

    return redirect('tasks:home')
