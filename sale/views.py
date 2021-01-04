from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Discount, Bonus
from django.urls import reverse


# Create your views here.

class Discounts(ListView):
    model = Discount
    template_name = 'adminlte/sales/discounts.html'


class AddDiscount(CreateView):
    model = Discount
    template_name = 'adminlte/sales/discount_form.html'
    fields = '__all__'
    paginate_by = 2


class DeleteDiscount(DeleteView):
    model = Discount
    template_name = 'adminlte/sales/delete_discount.html'

    def get_success_url(self):
        return reverse('adminPanel:admin_discounts')


class EditDiscount(UpdateView):
    model = Discount
    template_name = 'adminlte/sales/discount_form.html'
    fields = '__all__'


class Bonuses(ListView):
    model = Bonus
    template_name = 'adminlte/sales/bonuses.html'


class AddBonus(CreateView):
    model = Bonus
    template_name = 'adminlte/sales/bonus_form.html'
    fields = '__all__'


class EditBonus(UpdateView):
    model = Bonus
    template_name = 'adminlte/sales/bonus_form.html'
    fields = '__all__'


class DeleteBonus(DeleteView):
    model = Bonus
    template_name = 'adminlte/sales/delete_bonus.html'

    def get_success_url(self):
        return reverse('adminPanel:admin_bonuses')
