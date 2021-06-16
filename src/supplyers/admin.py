from django.contrib import admin

from .models import Supplier, Product_supplier

admin.site.register(Supplier)
admin.site.register(Product_supplier)