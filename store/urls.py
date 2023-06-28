from django.urls import path, include
from .  import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:slug>', views.product_details,name="product_details"),
    path('<str:slug>/add-to-cart/', views.add_to_cart,name="add_to_cart"),
    path('cart/', views.cart,name="cart"),
    path('cart/delete/', views.cart_delete,name="cart_delete"),


]