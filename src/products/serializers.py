from django.db import models
from rest_framework import serializers
# Models
from .models import Products

class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'
