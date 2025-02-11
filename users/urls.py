from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.signupView, name='signup'),
    path('signin/', views.signinView, name='signin'),
    path('signout/', views.signoutView, name='signout'),


]
