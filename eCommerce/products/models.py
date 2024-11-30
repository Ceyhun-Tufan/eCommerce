from django.db import models
from customers.models import Seller


class Product(models.Model):
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    name = models.CharField(max_length=80,blank=False,null=False)
    description = models.TextField(max_length=255,blank=True,null=True)
    price = models.DecimalField(max_digits=10,null=False,decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField("products/",blank=True,null=True,)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name


# Create your models here.
