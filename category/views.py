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


def get_categories():
    choices = ((None, 'دسنه بندی پدر را انتخاب کنید'),)
    categories = Category.objects.all()
    for category in categories:
        choices += ((category.id, category.title),)
    return choices


class CategoryForm(forms.ModelForm):
    parent = forms.ChoiceField(choices=get_categories())

    class Meta:
        model = Category
        fields = ['title', 'type', 'parent']

    # replace Category object with category id provided by template(user choice)
    def clean(self):
        for field, value in self.cleaned_data.items():
            if field == 'parent':
                self.cleaned_data['parent'] = Category.objects.get(id=value)


class AddCategory(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'adminlte/categories/category_form.html'


class EditCategory(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'adminlte/categories/category_form.html'


class DeleteCategory(DeleteView):
    model = Category
    template_name = 'adminlte/categories/delete_category.html'

    def get_success_url(self):
        return reverse('adminPanel:admin_categories')


class AddProductFamily(CreateView):
    model = ProductFamily
    fields = '__all__'
    template_name = 'adminlte/categories/productfamily_form.html'


class ProductFamilies(ListView):
    model = ProductFamily
    template_name = 'adminlte/categories/productfamilies.html'


class EditProductFamily(UpdateView):
    model = ProductFamily
    fields = '__all__'
    template_name = 'adminlte/categories/productfamily_form.html'


class DeleteProductFamily(DeleteView):
    model = ProductFamily
    template_name = 'adminlte/categories/delete_productfamily.html'

    def get_success_url(self):
        return reverse('adminPanel:admin_productfamilies')
