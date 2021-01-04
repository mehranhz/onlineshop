from django.db import models
from products.models import Product
from user.models import User
from category.models import ProductFamily
from django.urls import reverse


# Create your models here.

class Sale(models.Model):
    title = models.CharField(max_length=256)
    percentage = models.IntegerField(default=0)
    expire_date = models.DateField()
    slug = models.CharField(max_length=256)
    products = models.ManyToManyField(Product)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.CharField(max_length=128, null=True)


class Discount(models.Model):
    code = models.CharField(max_length=256, verbose_name="کد")
    percentage = models.IntegerField(verbose_name="درصد")
    maximum = models.IntegerField(verbose_name="ماکسیموم")
    cart_limitation = models.IntegerField(verbose_name="حداقل مبلغ سبد خرید")
    expire_date = models.DateField(verbose_name="تاریخ انقضا")
    creator = models.ForeignKey(User, on_delete=models.PROTECT, null=True, verbose_name="")
    status = models.CharField(max_length=128, null=True, verbose_name="وضعیت")

    def get_absolute_url(self):
        return reverse('adminPanel:admin_discounts')


class Bonus(models.Model):
    code = models.CharField(max_length=256, verbose_name="کد")
    amount = models.IntegerField(verbose_name="مبلغ")
    product_family = models.ForeignKey(ProductFamily, on_delete=models.PROTECT, null=True,
                                       verbose_name="دسته محصولات")
    expire_date = models.DateField(verbose_name="تاریخ انقضا")
    cart_limitation = models.IntegerField(default=0, verbose_name="حداقل مبلغ سبد خرید")
    creator = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="ایجاد کننده")
    status = models.CharField(max_length=128, null=True, verbose_name="وضعیت")

    def get_absolute_url(self):
        return reverse('adminPanel:admin_bonuses')
