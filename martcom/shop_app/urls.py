from django.urls import path
from .views import products
from . import views


urlpatterns = [
    path("products/", products, name="products"),
]
