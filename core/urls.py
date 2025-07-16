from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r"products", ProductsView, "products")
router.register(r"category", CategoryView, "category")
router.register(r"pedidos", PedidosView, "pedidos")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("", frontend)
]