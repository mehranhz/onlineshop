from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Category, ProductFamily
from django import forms
from django.urls import reverse


# Create your views here.

class Categoryy(DetailView):
    model = Category
    template_name = 'adminlte/categories/category.html'


class Categories(ListView):
    paginate_by = 10
    model = Category
    template_name = 'adminlte/categories/categories.html'


class AddCategory(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'adminlte/categories/category_form.html'


class EditCategory(UpdateView):
    model = Category
    template_name = 'adminlte/categories/category_form.html'


class DeleteCategory(DeleteView):
    model = Category
    template_name = 'adminlte/categories/delete_category.html'

    def get_success_url(self):
        return reverse('adminPanel:admin_categories')


class ProductFamilies(ListView):
    model = ProductFamily
    template_name = 'adminlte/categories/productfamilies.html'


class AddProductFamily(CreateView):
    model = ProductFamily
    fields = '__all__'
    template_name = 'adminlte/categories/productfamily_form.html'


class EditProductFamily(UpdateView):
    model = ProductFamily
    fields = '__all__'
    template_name = 'adminlte/categories/productfamily_form.html'


class DeleteProductFamily(DeleteView):
    model = ProductFamily
    template_name = 'adminlte/categories/delete_productfamily.html'

    def get_success_url(self):
        return reverse('adminPanel:admin_productfamilies')
