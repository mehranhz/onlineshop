from django.shortcuts import render
from .models import Order
from django.views.generic import ListView, CreateView
from django import forms


# Create your views here.

class Orders(ListView):
    model = Order
    template_name = 'adminlte/orders/orders.html'


class OrderForm(forms.ModelForm):
    search = forms.CharField()
    products = forms.CharField()

    class Meta:
        model = Order
        fields = []


class AddOrder(CreateView):
    model = Order
    template_name = 'adminlte/orders/order_form.html'
    form_class = OrderForm
