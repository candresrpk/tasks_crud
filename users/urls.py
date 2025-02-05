from django.urls import path
from . import views

app_name = 'crud_users'

urlpatterns = [
    path('signup/', views.signupView, name='signup'),
]
