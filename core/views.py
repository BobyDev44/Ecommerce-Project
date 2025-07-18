from django.shortcuts import render
from .serializers import *
from .models import Products, Category
from rest_framework import viewsets
from django.views.generic import TemplateView

# Create your views here.

def frontend(request):
    return render(request, "index.html")

class ProductsView(viewsets.ModelViewSet):
    serializer_class = ProductsSerializers
    queryset = Products.objects.all()

    # Filtrar productos por categoría
    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.request.query_params.get("category")
        if category_id:
            queryset = queryset.filter(category_id=category_id)
            #http://127.0.0.1:8000/api/v1/products/?category=1

        product_name = self.request.query_params.get("name")
        if product_name:
            queryset = queryset.filter(name__icontains=product_name)
            #http://127.0.0.1:8000/api/v1/products/?name=queso

        return queryset

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()

class PedidosView(viewsets.ModelViewSet):
    serializer_class = PedidosSerializers
    queryset = Pedido.objects.all()