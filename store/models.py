from django.db import models
from django.urls import reverse
from django.utils import timezone

from shop.settings import AUTH_USER_MODEL

# Create your models here.

"""
Product
-nom
-prix
-quantité en stock
-description
-image

"""

class Product(models.Model):
    name=models.CharField(max_length=128)
    slug=models.SlugField(max_length=128)
    price=models.FloatField(default=0.0)
    stock=models.IntegerField(default=0)
    description=models.TextField(blank=True)
    thumbnail=models.ImageField(upload_to="products",blank=True,null=True)

    def __str__(self):
        return f"{self.name}({self.stock})"

    def get_absolute_url(self):
        return reverse("product_details", kwargs={'slug':self.slug})

#Article (Order)
"""
Utilisateur
Produits
quantités
commandé ou non
"""
class Order(models.Model):
    user=models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    ordered=models.BooleanField(default=False)
    order_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

#Panier(Cart)
"""
utilisateur
Articles
commandé ou non
date de  la commande
"""
class Cart(models.Model):
    user=models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders=models.ManyToManyField(Order)

    def __str__(self):
        return self.user.username

    def delete(self, *args,**kwargs):
        orders=self.orders.all()
        for order in orders:
            order.ordered=True
            order.order_date=timezone.now()
            order.save()
        self.orders.clear()

        super().delete(*args,**kwargs)


