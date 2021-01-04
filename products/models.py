from django.db import models
from user.models import User
from category.models import Category, Brand
from filter.models import SpecificationList
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام محصول')
    thumbnail = models.CharField(max_length=255, null=True, verbose_name='تصویر اصلی')
    description = models.TextField(null=True, verbose_name='توضیحات')
    main_features = models.TextField(null=True, verbose_name='ویژگی های اصلی')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, verbose_name='دسته بندی')
    brand = models.CharField(max_length=128, null=True, verbose_name='برند')
    images = models.TextField(null=True, verbose_name='تصاویر')

    specifications = models.ForeignKey(SpecificationList, on_delete=models.PROTECT, null=True, verbose_name='لیست مشخصات')

    sale_count = models.IntegerField(default=0, null=True, verbose_name='تعداد فروش')
    total_count = models.IntegerField(default=0, null=True, verbose_name='تعداد کل')
    available = models.IntegerField(default=0, null=True, verbose_name='موجود')

    satisfaction = models.FloatField(default=0, null=True, verbose_name='میزان رضایت')
    vote_counts = models.IntegerField(default=0, null=True, verbose_name='تعداد آرا')

    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, verbose_name='کاربر')

    comment_count = models.IntegerField(default=0, null=True, verbose_name='تعداد نظرات')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('adminPanel:admin_product', kwargs={'pk': self.pk})


# class Gallery:

class ProductInstance(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    features = models.TextField(null=True)
    count = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)

    def __str__(self):
        return self.product.name+str(self.features)

    def get_absolute_url(self):
        return reverse('adminPanel:admin_products')
