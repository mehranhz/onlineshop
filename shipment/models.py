from django.db import models
from user.models import Address, Agent


class Shipment(models.Model):
    date = models.DateField()
    status = models.CharField(max_length=256)
    address = models.ForeignKey(Address, on_delete=models.PROTECT)
    release_date = models.DateField()
    note = models.TextField()
    agent = models.ForeignKey(Agent, on_delete=models.PROTECT)
