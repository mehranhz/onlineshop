from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=256, verbose_name="عنوان")
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, verbose_name="پدر")
    type = models.CharField(max_length=128, verbose_name="نوع")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('adminPanel:admin_categories')


class Brand(models.Model):
    title = models.CharField(max_length=128)


class ProductFamily(models.Model):
    categories = models.ManyToManyField(Category)

    def get_absolute_url(self):
        return reverse('adminPanel:admin_productfamilies')

    def __str__(self):

        categories = ''
        for category in self.categories.all():
            categories += category.title+' '
        return categories
