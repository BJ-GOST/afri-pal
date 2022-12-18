from django.db import models
from Jobs.models import *

# Create your models here.
class Transaction(models.Model):
    client = models.CharField(max_length=255, null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField(null=True)
    day = models.DateField(auto_now_add=True, null=True)
    time = models.TimeField(auto_now_add=True, null=True)
