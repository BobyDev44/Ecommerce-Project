from django.contrib import admin
from .models import *

# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    list_filter = ["fecha"]
    search_fields = ["nombre", "telefono"]

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Pedido, PedidoAdmin)