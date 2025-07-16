from django.urls import path
from .views import *
urlpatterns = [
    path("", home, name="home"),
    path("registro/", registro, name="registro"),
    path("crearsuperuser021107/", registrosuper, name="crearsuperuser021107"),
    path("iniciarsesion/", iniciarsesion, name="iniciarsesion"),
    path("cerrarsesion/", cerrarsesion, name="cerrarsesion"),
]