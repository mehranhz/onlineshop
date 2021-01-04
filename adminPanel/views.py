from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from products.models import Product
from django import forms


# index page of admin panel(dashboard)
def Index(request):
    return render(request, 'adminlte/index.html')


def Register(request):
    return render(request, 'adminlte/register.html')


def Calender(request):
    return render(request, 'adminlte/calender.html')

