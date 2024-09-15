from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe

from item.models import Item


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Order(models.Model):
    STATUS = (('New', 'New'),
              ('Accepted', 'Accepted'),
              ('Preparing', 'Preparing'),
              ('OnShipping', 'OnShipping'),
              ('Completed', 'Completed'),
              ('Canceled', 'Canceled'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
