from django.urls import path
from . import views


app_name = 'tasks'

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('create/', views.createTask, name='create'),

]
