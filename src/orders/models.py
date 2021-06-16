from django.db import models
from django.contrib.auth.models import User
from products.models import Products
# Models

class Orders (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'id:{self.id} user:{self.user}'

class Orders_Items(models.Model):
    order = models.ForeignKey(Orders, null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Products, null=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'id:{self.id} product:{self.product}, qty:{self.quantity}'