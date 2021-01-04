from django.shortcuts import render
from .models import User
from django.views.generic import ListView, CreateView


class Users(ListView):
    model = User
    template_name = 'adminlte/users/users.html'


# class AddUser(CreateUser):
#     model = User
#     template_name = 'adminlte/users/user_form.html'
