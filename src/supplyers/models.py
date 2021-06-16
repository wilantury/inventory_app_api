from django.db import models
# Models
from profiles.models import City
from products.models import Products

class Supplier(models.Model):
    supplier_id = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=180)
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=14)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'CN: {self.company_name}'

class Product_supplier(models.Model):
    product = models.ForeignKey(Products,null=True ,on_delete=models.SET_NULL)
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL)
