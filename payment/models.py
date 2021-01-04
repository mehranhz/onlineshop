from django.db import models
from user.models import User


class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    balance = models.IntegerField()


class CreditCard(models.Model):
    code = models.CharField(max_length=20)
    amount = models.FloatField()
    status = models.CharField(max_length=255)
    created_at = models.DateField()
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    password = models.CharField(max_length=500)
    expire_date = models.DateField()
