from django.shortcuts import render
from django.views.generic import View, CreateView, UpdateView, DetailView, ListView, DeleteView
from products.models import Product, ProductInstance
from django.urls import reverse
from django import forms
import json


class Products(ListView):
    model = Product
    paginate_by = 1
    template_name = 'adminlte/products/products.html'


class AddProduct(CreateView):
    fields = [
        'name',
        'brand',
        'thumbnail',
        'main_features',
        'description',
        'total_count',
        'available',
        'category',
        'images'
    ]
    model = Product
    template_name = 'adminlte/products/product_form.html'

    def form_valid(self, form):
        # convert images list to json
        list = []
        images = form.instance.images.splitlines()
        if not images == "":
            for item in images:
                list.append(json.loads(item))
            form.instance.images = {"images": list}
        else:
            form.instance.images = {"images": ""}
        feature_list = []
        features = form.instance.main_features.splitlines()
        for item in features:
            feature_list.append(item)
        form.instance.main_features = feature_list
        return super().form_valid(form)


class UpdateProduct(UpdateView):
    fields = [
        'name',
        'brand',
        'thumbnail',
        'main_features',
        'description',
        'total_count',
        'available',
        'category',
        'images'
    ]
    model = Product
    template_name = 'adminlte/products/product_form.html'

    def form_valid(self, form):
        # convert images list to json
        list = []
        images = form.instance.images.splitlines()
        if not images == " ":
            for item in images:
                list.append(json.loads(item))
            form.instance.images = {"images": list}
        else:
            form.instance.images = {"images": " "}
        feature_list = []
        features = form.instance.main_features.splitlines()
        for item in features:
            feature_list.append(item)
        form.instance.main_features = feature_list
        return super().form_valid(form)

    def get_initial(self, **kwargs):
        product = self.get_object()
        features = json.loads(product.main_features.replace("'", ""))
        initial = super(UpdateProduct, self).get_initial()
        images = ProductView.images(product)['images']
        str_images = ''
        str_features = ''
        for feature in features:
            str_features += json.dumps(feature, ensure_ascii=False).encode('utf8').decode() + "\n"
        for item in images:
            str_images += json.dumps(item, ensure_ascii=False).encode('utf8').decode() + "\n"

        initial['images'] = str_images
        initial['main_features'] = str_features
        return initial


class DeleteProduct(DeleteView):
    model = Product
    template_name = 'adminlte/products/delete_product.html'

    def get_success_url(self):
        return reverse('adminPanel:admin_products')


class ProductView(DetailView):
    template_name = 'adminlte/products/product.html'
    model = Product

    @staticmethod
    def images(product):
        if product.images:
            # replacing ' with " to prevent error in json.loads function
            images = product.images.replace("'", '"')
            return json.loads(images)
        else:
            return "no image"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main_features"] = json.loads(context["product"].main_features.replace("'", ''))
        # take different instances of product
        context['instances'] = ProductInstance.objects.filter(product=self.kwargs['pk'])
        # take replace products images in json format with string format
        context["images"] = self.images(context["product"])
        return context


class AddInstance(CreateView):
    model = ProductInstance
    template_name = 'adminlte/products/product.html'
    fields = ('features', 'count')

    def get_success_url(self):
        context = self.get_context_data(object=self.object)
        return reverse('adminPanel:admin_product', kwargs={'pk': context['product'].id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(id=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.product = self.get_context_data()['product']
        return super().form_valid(form)


class UpdateInstance(UpdateView):
    model = ProductInstance
    template_name = 'adminlte/products/product.html'
    fields = ('count', 'features')

    def get_success_url(self):
        context = self.get_context_data(object=self.object)
        return reverse('adminPanel:admin_product', kwargs={'pk': context['product'].id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(id=self.kwargs['product'])
        context['instance'] = ProductInstance.objects.get(id=self.kwargs['pk'])
        return context


class DeleteInstance(DeleteView):
    model = ProductInstance
    template_name = 'adminlte/products/delete_instance.html'

    def get_success_url(self):
        context = self.get_context_data(object=self.object)
        return reverse('adminPanel:admin_product', kwargs={'pk': context['product'].id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Product.objects.get(id=self.kwargs['product'])
        context['instance'] = ProductInstance.objects.get(id=self.kwargs['pk'])
        return context
