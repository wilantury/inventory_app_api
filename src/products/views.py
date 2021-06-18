from rest_framework.generics import ListAPIView
# serializers
from .serializers import ProductsSerializer
# Models
from .models import Products


class ProductsList(ListAPIView):
    serializer_class = ProductsSerializer

    def get_queryset(self):
        return Products.objects.all()
