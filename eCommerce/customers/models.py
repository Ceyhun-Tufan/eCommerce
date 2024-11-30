from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15,blank=True,null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Seller(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)