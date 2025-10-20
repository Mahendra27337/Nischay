from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
class ReferralCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=32, unique=True)
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
class AreaFranchise(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    area_name = models.CharField(max_length=200)
class Shop(models.Model):
    franchise = models.ForeignKey(AreaFranchise, on_delete=models.CASCADE, related_name='shops')
    name = models.CharField(max_length=200)
    address = models.TextField(blank=True)
