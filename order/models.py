from django.db import models
from user.models import User, Address
from shipment.models import Shipment
from sale.models import Discount, Bonus
from products.models import ProductInstance


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateField()
    status = models.CharField(max_length=128)
    payment_status = models.CharField(max_length=128)
    products = models.ManyToManyField(ProductInstance, through='OrderProduct')
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    shipment = models.ForeignKey(Shipment, on_delete=models.PROTECT)


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductInstance, models.CASCADE)
    number = models.IntegerField(default=0)


class Receipt(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    fee = models.FloatField()
    discount = models.ForeignKey(Discount, on_delete=models.PROTECT)
    bonus = models.ForeignKey(Bonus, on_delete=models.PROTECT)
    total_discount = models.FloatField()
    final_fee = models.FloatField()
    date = models.DateField()
    status = models.CharField(max_length=128)
