from django.urls import path
# Views
from .views import ProductsList

app_name = 'products'

urlpatterns = [
    path('products/', ProductsList.as_view(), name='products_list')
]
