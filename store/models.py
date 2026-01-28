from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100) # название
    price = models.IntegerField() # цена
    description = models.TextField(blank=True) # описание (необязательно)


def __str__(self):
    return self.name