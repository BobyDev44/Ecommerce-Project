from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField

# Create your models here.
    
def get_image_field():
    if settings.DEBUG:
        return models.ImageField(upload_to="products")
    else:
        return CloudinaryField("image")
    
def get_image_category_field():
    if settings.DEBUG:
        return models.ImageField(upload_to="categories")
    else:
        return CloudinaryField("image")

class Category(models.Model):
    category = models.CharField(max_length=50)
    #image = get_image_category_field()
    

    def __str__(self):
        return self.category

class Products(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    image = get_image_field()
    details = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.name

class Pedido(models.Model):
    entregado = models.BooleanField(default=False)
    nombre = models.CharField(max_length=200)
    telefono = models.IntegerField()
    direccion = models.TextField()
    productos = models.TextField()
    otros = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(decimal_places=2, max_digits=20, default=0)

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return f"{self.entregado} - Pedido {self.id} - Cliente: {self.nombre} - {self.telefono}"