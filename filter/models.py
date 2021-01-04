from django.db import models
from category.models import Category


class Specification(models.Model):
    key = models.CharField(max_length=256)  # remember to define a message key for attaching a note to a product
    value = models.CharField(max_length=256)
    category = models.ForeignKey(Category, null=True,on_delete=models.PROTECT)
    type = models.CharField(max_length=128)


class SpecificationList(models.Model):
    specification = models.ManyToManyField(Specification)
