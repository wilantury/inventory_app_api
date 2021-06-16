from django.db import models

class Products(models.Model):
    product_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=300, blank=True, null=True)
    image = models.ImageField(upload_to='products', default='no_picture.png')
    quantity = models.PositiveIntegerField()
    price = models.FloatField(help_text='En Pesos colombianos')
    unit_measure = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'id:{self.id} name: {self.name} price:{self.price} qty:{self.quantity}'


